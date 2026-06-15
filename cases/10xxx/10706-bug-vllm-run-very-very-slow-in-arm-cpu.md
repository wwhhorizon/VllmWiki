# vllm-project/vllm#10706: [Bug]: VLLM run very very slow in ARM cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#10706](https://github.com/vllm-project/vllm/issues/10706) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM run very very slow in ARM cpu

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I build the docker file using dockerfile.arm , it is Unbearable slow. details: `Avg prompt throughput: 0.5 tokens/s, Avg generation throughput: 0.3 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%.` . The command I start the the container: `docker run -it --rm --net=host -v /root/models:/models -e VLLM_CPU_KVCACHE_SPACE=1 -e TRITON_F32_DEFAULT=ieee --memory="4G" --cpuset-cpus="32-35" --cpuset-mems="1" --name=vllm-arm-4c4g vllm_for_arm:v2 --model /models/qwen2.5-0.5b-instruct/ --device cpu --trust-remote-code --dtype=float32` Does vllm support ARM cpu properly? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I build the docker file using dockerfile.arm , it is Unbearable slow. details: `Avg prompt throughput: 0.5 tokens/s, Avg generation throughput: 0.3 tokens/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -model /models/qwen2.5-0.5b-instruct/ --device cpu --trust-remote-code --dtype=float32` Does vllm support ARM cpu properly? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ly? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: very very slow in ARM cpu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I build the docker file using dockerfile.arm , it is Unbearable slow. details: `Avg prompt thro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: VLLM run very very slow in ARM cpu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I build the docker file using dockerfile.arm , it is Unbearable slow. details:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
