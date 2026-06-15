# vllm-project/vllm#1835: In LLM, how do I make a model streaming output?

| 字段 | 值 |
| --- | --- |
| Issue | [#1835](https://github.com/vllm-project/vllm/issues/1835) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> In LLM, how do I make a model streaming output?

### Issue 正文摘录

``` model_path = r'/Yi-34B-Chat/' def load_model(model_name, tp_size=4): llm = LLM(model_name, tensor_parallel_size=tp_size, tokenizer_mode='auto', trust_remote_code=True) return llm def main( model, max_new_tokens=100, user_prompt=None, top_p=0.9, temperature=0.8 ): while True: if user_prompt is None: user_prompt = input("Enter your prompt: ") print(f"User prompt:\n{user_prompt}") print(f"sampling params: top_p {top_p} and temperature {temperature} for this inference request") sampling_param = SamplingParams(top_p=top_p, temperature=temperature, max_tokens=max_new_tokens) outputs = model.generate(user_prompt, sampling_params=sampling_param) print(f"model output:\n {user_prompt} {outputs[0].outputs[0].text}") user_prompt = input("Enter next prompt (press Enter to exit): ") if not user_prompt: break def run_script( model_name=model_path, peft_model=None, tp_size=2, max_new_tokens=256, user_prompt=None, top_p=0.9, temperature=0.8 ): model = load_model(model_name, tp_size) main(model, max_new_tokens, user_prompt, top_p, temperature) if __name__ == "__main__": fire.Fire(run_script) ``` I'm using the code above and I'm finding that I can't get the model to stream output.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: In LLM, how do I make a model streaming output? ``` model_path = r'/Yi-34B-Chat/' def load_model(model_name, tp_size=4): llm = LLM(model_name, tensor_parallel_size=tp_size, tokenizer_mode='auto', trust_remote_code=True)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g params: top_p {top_p} and temperature {temperature} for this inference request") sampling_param = SamplingParams(top_p=top_p, temperature=temperature, max_tokens=max_new_tokens) outputs = model.generate(user_prompt, s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
