# vllm-project/vllm#25859: [Bug] [version 0.10.1]: Qwen2.5-VL online request template error

| 字段 | 值 |
| --- | --- |
| Issue | [#25859](https://github.com/vllm-project/vllm/issues/25859) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [version 0.10.1]: Qwen2.5-VL online request template error

### Issue 正文摘录

### Your current environment vllm==0.10.1 xformers==0.32.0 torch==2.7.1 transformers==4.56.1 ### 🐛 Describe the bug **When deploying the OpenAI-compatible service with vLLM version 0.7.3 using the Qwen2.5-VL model, responses are returned successfully. However, when using vLLM version 0.10.1, the model produces the following error: 当使用0.7.3版本的vllm为qwen2.5-vl部署openai服务时，通过以下数据形式可以正常请求，但是当将vllm升级为0.10.1版本时，会报错。** - 数据格式： - 错误： - 启动命令 `CUDA_VISIBLE_DEVICES=0,1,2,3 python3.10 -m vllm.entrypoints.openai.api_server --served-model-name Qwen2.5-VL-32B --model Qwen2.5-VL-32B --gpu-memory-utilization 0.85 --tensor-parallel-size 4 --port 8787` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 过以下数据形式可以正常请求，但是当将vllm升级为0.10.1版本时，会报错。** - 数据格式： - 错误： - 启动命令 `CUDA_VISIBLE_DEVICES=0,1,2,3 python3.10 -m vllm.entrypoints.openai.api_server --served-model-name Qwen2.5-VL-32B --model Qwen2.5-VL-32B --gpu-memory-utiliz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] [version 0.10.1]: Qwen2.5-VL online request template error bug ### Your current environment vllm==0.10.1 xformers==0.32.0 torch==2.7.1 transformers==4.56.1 ### 🐛 Describe the bug **When deploying the OpenAI-compat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug] [version 0.10.1]: Qwen2.5-VL online request template error bug ### Your current environment vllm==0.10.1 xformers==0.32.0 torch==2.7.1 transformers==4.56.1 ### 🐛 Describe the bug **When deploying the OpenAI-compat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug] [version 0.10.1]: Qwen2.5-VL online request template error bug ### Your current environment vllm==0.10.1 xformers==0.32.0 torch==2.7.1 transformers==4.56.1 ### 🐛 Describe the bug **When deploying the OpenAI-compat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
