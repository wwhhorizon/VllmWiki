# vllm-project/vllm#11526: [Bug]: Different sampled output when running on different GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#11526](https://github.com/vllm-project/vllm/issues/11526) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Different sampled output when running on different GPUs

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` from openai import OpenAI import sys if __name__ == "__main__": port = sys.argv[1] client = OpenAI(base_url=f"http://0.0.0.0:{port}/v1") gen_func = client.chat.completions.create transformers.set_seed(42) np.random.seed(42) torch.manual_seed(42) args = { "model": "meta-llama/Meta-Llama-3.1-8B-Instruct", "messages": [{"role": "user", "content": "Give a speech on abortion"}],, "seed": 892, "max_tokens": 250, "temperature": 0.7 } completion = gen_func(**args) print(completion.choices[0].message.content) ``` When running on different type of GPU, i.e. a100 versus h100, I would obtain different results. How I ran the servers: ``` CUDA_VISIBLE_DEVICES=$GPU python -m vllm.entrypoints.openai.api_server \ --model $model --max_model_len 6144 --guided-decoding-backend lm-format-enforcer \ --tensor-parallel-size 1 --port $PORT & ``` But if I set temperature = 0.0 would be fine ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ces[0].message.content) ``` When running on different type of GPU, i.e. a100 versus h100, I would obtain different results. How I ran the servers: ``` CUDA_VISIBLE_DEVICES=$GPU python -m vllm.entrypoints.openai.api_serv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: running on different GPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` from openai import OpenAI import sys if __name__ == "__main__": port = sys.argv[1] client =...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: api_server \ --model $model --max_model_len 6144 --guided-decoding-backend lm-format-enforcer \ --tensor-parallel-size 1 --port $PORT & ``` But if I set temperature = 0.0 would be fine ### Before submitting a new issue....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: odel Input Dumps _No response_ ### 🐛 Describe the bug ``` from openai import OpenAI import sys if __name__ == "__main__": port = sys.argv[1] client = OpenAI(base_url=f"http://0.0.0.0:{port}/v1") gen_func = client.chat.c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Different sampled output when running on different GPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` from openai import OpenAI import sys if __name__ == "_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
