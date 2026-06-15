# vllm-project/vllm#10971: [Bug]: Vllm CPU mode only takes 1 single core for multi-core cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#10971](https://github.com/vllm-project/vllm/issues/10971) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm CPU mode only takes 1 single core for multi-core cpu

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . sudo docker run --env "VLLM_CPU_KVCACHE_SPACE=10" --env "VLLM_CPU_OMP_THREADS_BIND=0,2,4,6,8,10,12,14,16-26" --privileged=true --ipc=host vllm-cpu-env --model "meta-llama/Llama-3.2-1B-Instruct" --max-model-len "4096" ``` And run it, and even if there are many concurrent requests, vllm takes 1 single core (instead of e.g. 10 cores) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . sudo docker run --env "VLLM_CPU_KVCACHE_SPACE=10" --env "VLLM_CPU_OMP_THREADS_BIND=0,2,4,6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Vllm CPU mode only takes 1 single core for multi-core cpu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker build -f Dockerfile.cpu -t vllm-cpu-env --shm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e core for multi-core cpu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . sudo docker run --env "VLLM_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;spec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
