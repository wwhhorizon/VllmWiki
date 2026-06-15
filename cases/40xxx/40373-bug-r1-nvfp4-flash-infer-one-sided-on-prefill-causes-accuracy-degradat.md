# vllm-project/vllm#40373: [Bug]: R1 NVFP4 flash_infer_one_sided on prefill causes accuracy degradation during P/D

| 字段 | 值 |
| --- | --- |
| Issue | [#40373](https://github.com/vllm-project/vllm/issues/40373) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: R1 NVFP4 flash_infer_one_sided on prefill causes accuracy degradation during P/D

### Issue 正文摘录

### Your current environment The deployment config can be found in [PD](https://github.com/tlrmchlsmth/j-llm-d/tree/r1nvfp4-pd-defaults/gb200/base). With the change of a2a backend to `--all2all-backend "flash_infer_one_sided" \ ` in prefill.yaml [here](https://github.com/tlrmchlsmth/j-llm-d/blob/r1nvfp4-pd-defaults/gb200/base/prefill.yaml#L122). With `deepep_high_throughput`, the accuracy is stable at around 96.3%. ### 🐛 Describe the bug The accuracy goes down to about 92.9% from the usual 96.3%. **Important**: `flash_infer_one_sided` does not cause an accuracy drop when used for decode. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nt The deployment config can be found in [PD](https://github.com/tlrmchlsmth/j-llm-d/tree/r1nvfp4-pd-defaults/gb200/base). With the change of a2a backend to `--all2all-backend "flash_infer_one_sided" \ ` in prefill.yaml...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: R1 NVFP4 flash_infer_one_sided on prefill causes accuracy degradation during P/D bug ### Your current environment The deployment config can be found in [PD](https://github.com/tlrmchlsmth/j-llm-d/tree/r1nvfp4-pd-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: R1 NVFP4 flash_infer_one_sided on prefill causes accuracy degradation during P/D bug ### Your current environment The deployment config can be found in [PD](https://github.com/tlrmchlsmth/j-llm-d/tree/r1nvfp4-pd-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: R1 NVFP4 flash_infer_one_sided on prefill causes accuracy degradation during P/D bug ### Your current environment The deployment config can be found in [PD](https://github.com/tlrmchlsmth/j-llm-d/tree/r1nvfp4-pd-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: th/j-llm-d/tree/r1nvfp4-pd-defaults/gb200/base). With the change of a2a backend to `--all2all-backend "flash_infer_one_sided" \ ` in prefill.yaml [here](https://github.com/tlrmchlsmth/j-llm-d/blob/r1nvfp4-pd-defaults/gb...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
