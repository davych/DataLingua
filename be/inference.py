"""
本文件为 HuggingFace Transformers 推理封装（HFInference类），可直接用于本地大模型 SQL 生成。

注意：本代码在 Mac M3 (36G) 上实测可跑通，
但即使 MPS 支持，加载如 sqlcoder-7b-2 这类大模型时依然极易爆内存。
简单输入都需要等5分钟才有结果，复杂输入直接崩。

代码先放着，sqlcoder的测试 -仍然用ollama 下的模型跑
"""


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class HFInference:
    def __init__(self, model_name="defog/sqlcoder-7b-2"):
        self.prompt_file = "prompt.md"
        self.metadata_file = "metadata.sql"
        self.model_name = model_name
        self.tokenizer, self.model = self._load_model_and_tokenizer(model_name)

    def _load_model_and_tokenizer(self, model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            torch_dtype=torch.float16,
            device_map="auto",
            use_cache=True,
        )
        return tokenizer, model

    def generate_prompt(self, question, prompt_file="prompt_sql.md", metadata_file="metadata.sql"):
        with open(prompt_file, "r") as f:
            prompt = f.read()
        with open(metadata_file, "r") as f:
            table_metadata_string = f.read()
        prompt = prompt.format(
            user_question=question, table_metadata_string=table_metadata_string
        )
        return prompt

    def generate_sql(self, question):
        prompt = self.generate_prompt(question, self.prompt_file, self.metadata_file)
        print("Prompting model...", prompt)
        eos_token_id = self.tokenizer.eos_token_id
        pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=300,
            do_sample=False,
            return_full_text=False,
            num_beams=5,
        )
        generated_query = (
            pipe(
                prompt,
                num_return_sequences=1,
                eos_token_id=eos_token_id,
                pad_token_id=eos_token_id,
            )[0]["generated_text"]
            .split(";")[0]
            .split("```")[0]
            .strip()
            + ";"
        )
        return generated_query

# if __name__ == "__main__":
#     # Parse arguments
#     _default_question="Do we get more sales from customers in New York compared to customers in San Francisco? Give me the total sales for each city, and the difference between the two."
#     parser = argparse.ArgumentParser(description="Run inference on a question")
#     parser.add_argument("-q","--question", type=str, default=_default_question, help="Question to run inference on")
#     args = parser.parse_args()
#     question = args.question
#     print("Loading a model and generating a SQL query for answering your question...")
#     print(run_inference(question))
