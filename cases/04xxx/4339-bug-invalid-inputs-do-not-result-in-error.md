# vllm-project/vllm#4339: [Bug]: Invalid inputs do not result in error

| 字段 | 值 |
| --- | --- |
| Issue | [#4339](https://github.com/vllm-project/vllm/issues/4339) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Invalid inputs do not result in error

### Issue 正文摘录

### Your current environment Start vLLM: ```docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model gpt2 --dtype float16 --max-model-len 1024``` ### 🐛 Describe the bug When running inference with vLLM, errors are not returned when an invalid input is supplied. After starting vLLM as specified above, run a curl command that supplies invalid inputs: ```curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "gpt2", "messages": [ { "role": "system", "content": "You are a helpful assistant.", "fake_input": "2" }, { "role": "user", "content": "Hello!", "fake_input": "3" } ] }'``` You get a successful response. Fake_input is dropped instead of returning an error. This silent failure can be dangerous with typos or invalid inputs. Can this be fixed?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: do not result in error bug ### Your current environment Start vLLM: ```docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model gpt2 --dtype float16...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model gpt2 --dtype float16 --max-model-len 1024``` ### 🐛 Describe the bug When running inference with vLLM, errors are not returned when an invalid input is su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ur current environment Start vLLM: ```docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model gpt2 --dtype float16 --max-model-len 1024``` ### 🐛 Des...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: face:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model gpt2 --dtype float16 --max-model-len 1024``` ### 🐛 Describe the bug When running inference with vLLM, errors are not returned when an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
