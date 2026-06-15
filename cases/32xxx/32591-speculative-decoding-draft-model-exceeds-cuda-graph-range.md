# vllm-project/vllm#32591: Speculative-Decoding Draft Model Exceeds Cuda Graph Range

| 字段 | 值 |
| --- | --- |
| Issue | [#32591](https://github.com/vllm-project/vllm/issues/32591) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Speculative-Decoding Draft Model Exceeds Cuda Graph Range

### Issue 正文摘录

### Your current environment [SD branch](https://github.com/vllm-project/vllm/pull/24322) ### 🐛 Describe the bug The scheduler schedules up to `max-num-batched-tokens` tokens (e.g. 2048), but during spec decoding with draft models we pass one extra token per sequence. This leads to a runtime error in CUDA graphs, because the sequence length was only captured up to 2048. # How to Reproduce ```shell vllm serve Qwen/Qwen3-4B \ --speculative_config.method draft_model \ --speculative_config.model Qwen/Qwen3-1.7B \ --speculative_config.num_speculative_tokens 4 \ --speculative_config.max_model_len 5000 \ --max-model-len 5000 \ --disable-uvicorn-access-log \ --no-enable-prefix-caching | tee serve.txt vllm bench serve \ --model Qwen/Qwen3-4B \ --dataset-name hf \ --dataset-path likaixin/InstructCoder \ --num-prompts 50 \ --max-concurrency 32 \ --temperature 0.0 \ --top-p 1.0 ``` Error: ```shell ... [0;36m(EngineCore_DP0 pid=1081641)[0;0m ERROR 01-19 11:58:38 [core.py:937] File "/home/tomasruiz/code/vllm/vllm/compilation/piecewise_backend.py", line 186, in __call__ [0;36m(EngineCore_DP0 pid=1081641)[0;0m ERROR 01-19 11:58:38 [core.py:937] assert range_entry is not None, ( [0;36m(Engine...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Speculative-Decoding Draft Model Exceeds Cuda Graph Range bug ### Your current environment [SD branch](https://github.com/vllm-project/vllm/pull/24322) ### 🐛 Describe the bug The scheduler schedules up to `max-num-batch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Speculative-Decoding Draft Model Exceeds Cuda Graph Range bug ### Your current environment [SD branch](https://github.com/vllm-project/vllm/pull/24322) ### 🐛 Describe the bug The scheduler schedules up to `max-num-batc
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Speculative-Decoding Draft Model Exceeds Cuda Graph Range bug ### Your current environment [SD branch](https://github.com/vllm-project/vllm/pull/24322) ### 🐛 Describe the bug The scheduler schedules up to `max-num-batch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ore.py:937] File "/home/tomasruiz/code/vllm/vllm/compilation/piecewise_backend.py", line 186, in __call__ [0;36m(EngineCore_DP0 pid=1081641)[0;0m ERROR 01-19 11:58:38 [core.py:937] assert range_entry is not None, ( [...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: phs, because the sequence length was only captured up to 2048. # How to Reproduce ```shell vllm serve Qwen/Qwen3-4B \ --speculative_config.method draft_model \ --speculative_config.model Qwen/Qwen3-1.7B \ --speculative_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
