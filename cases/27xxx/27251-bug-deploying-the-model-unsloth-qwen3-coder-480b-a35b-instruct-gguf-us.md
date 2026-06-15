# vllm-project/vllm#27251: [Bug]: Deploying the model unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF using docker vllm/vllm-openai:v0.10.2 and vllm/vllm-openai:v0.11.0 failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#27251](https://github.com/vllm-project/vllm/issues/27251) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deploying the model unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF using docker vllm/vllm-openai:v0.10.2 and vllm/vllm-openai:v0.11.0 failed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### error desc: After vLLM successfully starts the model, when calling the model, vLLM immediately reports an error causing the service to crash and shut down. ### Startup command： `docker run -d --name Qwen3-Coder-480B-A35B-Instruct-GGUF --runtime nvidia --gpus '"device=0,1,2,3,4,5,6,7"' -v /xinference/my_model/Qwen3-Coder-480B-A35B-Instruct-GGUF:/root/.cache/modelscope/Qwen3-Coder-480B-A35B-Instruct-GGUF -p 8056:8081 --ipc=host swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/vllm/vllm-openai:v0.10.2 --api-key qwen3coder480b --model /root/.cache/modelscope/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-Q4_K_M-Merge.gguf --served-model-name Qwen3-Coder-480B-A35B-Instruct --enable-auto-tool-choice --tool-call-parser qwen3_coder --gpu-memory-utilization 0.85 --tensor-parallel-size 8 --reasoning-parser qwen3 --max-model-len 50000 --port 8081` ### vllm/vllm-openai:v0.10.2 error logs [vll_10_2.log](https://github.com/user-attachments/files/23015383/vll_10_2.log) ### vllm/vllm-openai:v0.11.0 error logs [vllm_11.log](https://github.com/user-attachments/files/23015139/vllm_11.log) ### Before submitting a new issue....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Deploying the model unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF using docker vllm/vllm-openai:v0.10.2 and vllm/vllm-openai:v0.11.0 failed. bug;stale ### Your current environment ### 🐛 Describe the bug ### error d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ]: Deploying the model unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF using docker vllm/vllm-openai:v0.10.2 and vllm/vllm-openai:v0.11.0 failed. bug;stale ### Your current environment ### 🐛 Describe the bug ### error desc:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: og) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Deploying the model unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF using docker vllm/vllm-openai:v0.10.2 and vllm/vllm-openai:v0.11.0 failed. bug;stale ### Your current environment ### 🐛 Describe the bug ### error d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: docker vllm/vllm-openai:v0.10.2 and vllm/vllm-openai:v0.11.0 failed. bug;stale ### Your current environment ### 🐛 Describe the bug ### error desc: After vLLM successfully starts the model, when calling the model, vLLM i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
