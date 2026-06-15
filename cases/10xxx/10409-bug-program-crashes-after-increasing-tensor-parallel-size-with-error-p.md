# vllm-project/vllm#10409: [Bug]: (Program crashes after increasing --tensor-parallel-size) with error pynvml.NVMLError_InvalidArgument: Invalid Argument 

| 字段 | 值 |
| --- | --- |
| Issue | [#10409](https://github.com/vllm-project/vllm/issues/10409) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (Program crashes after increasing --tensor-parallel-size) with error pynvml.NVMLError_InvalidArgument: Invalid Argument 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've tried downgrading the docker image and many other combinations, but if I just increase the --tensor-parallel-size argument (to 2 or 3), the application crashes. I missed all the deadlines and haven't run vllm on more than 1 GPU yet. Initial config: ``` docker run --runtime nvidia --gpus '"device=0,1"' \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /home/thinclient/llm-server/weights:/mnt/weights \ --env "HUGGING_FACE_HUB_TOKEN=MY_TOKEN" \ --env "CUDA_VISIBLE_DEVICES=2" \ -p 8000:8000 \ --ipc host \ vllm/vllm-openai:latest \ --model /mnt/weights/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.97 \ --max_model_len 3500 \ ``` Error: https://gist.github.com/JohnConnor123/555d5afd99ed68299a8d8226a8af7039 or if you prefer pastebin: https://pastebin.com/Vqc9seit Modifications: 1. After removing `--runtime nvidia` nothing is happened, error is the same. 2. After removing `--env "CUDA_VISIBLE_DEVICES=2"` error logs: https://gist.github.com/JohnConnor123/aa758c7070ca755d96d29e6e1ddaf407 or if you prefer pastebin: https://pastebin.com/62ceYeVw !...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Dumps _No response_ ### 🐛 Describe the bug I've tried downgrading the docker image and many other combinations, but if I just increase the --tensor-parallel-size argument (to 2 or 3), the application crashes. I missed a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: gument: Invalid Argument bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've tried downgrading the docker image and many other combinations, but if I just increase the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: :/mnt/weights \ --env "HUGGING_FACE_HUB_TOKEN=MY_TOKEN" \ --env "CUDA_VISIBLE_DEVICES=2" \ -p 8000:8000 \ --ipc host \ vllm/vllm-openai:latest \ --model /mnt/weights/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf \ --tensor-par...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: size) with error pynvml.NVMLError_InvalidArgument: Invalid Argument bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've tried downgrading the docker image and many othe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
