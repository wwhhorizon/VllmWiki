# vllm-project/vllm#44245: fix(lora): _load_lora_config retry uses deterministic backoff without jitter — thundering herd risk

| 字段 | 值 |
| --- | --- |
| Issue | [#44245](https://github.com/vllm-project/vllm/issues/44245) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> fix(lora): _load_lora_config retry uses deterministic backoff without jitter — thundering herd risk

### Issue 正文摘录

## Summary [Quorum](https://github.com/KaustubhUp025/quorum) detected a coordination anti-pattern in PR #34981 while reviewing the new `_load_lora_config` retry logic. ## The bug ```python # vllm/lora/peft_helper.py (added in PR #34981) interval = 0.05 max_interval = 1.0 while True: try: with open(path) as f: return json.load(f) except (FileNotFoundError, json.JSONDecodeError) as err: ... time.sleep(min(interval, max_interval, remaining)) interval *= 2 # ← deterministic doubling, no jitter ``` The backoff doubles deterministically: **50ms → 100ms → 200ms → 400ms → 800ms → 1000ms (cap)**. ## Why this is a problem When multiple vLLM workers simultaneously try to load the same LoRA adapter (e.g., during warmup when a batch of requests arrives for the same adapter), they all encounter the same `FileNotFoundError` at the same time (NFS flush race, HF Hub download delay, etc.). Because the backoff is deterministic, **all workers retry at exactly the same intervals**. The retry storm hits the filesystem or network resource in synchronized waves, potentially making a short transient blip into a sustained overload — a classic [thundering herd](https://aws.amazon.com/blogs/architecture/expo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: xponential-backoff-and-jitter/). ## Suggested fix Add full jitter (AWS Builders' Library recommendation): ```python import random time.sleep(random.uniform(0, min(interval, max_interval, remaining))) interval *= 2 ``` O...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: fix(lora): _load_lora_config retry uses deterministic backoff without jitter — thundering herd risk ## Summary [Quorum](https://github.com/KaustubhUp025/quorum) detected a coordination anti-pattern in PR #34981 while re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: return json.load(f) except (FileNotFoundError, json.JSONDecodeError) as err: ... time.sleep(min(interval, max_interval, remaining)) interval *= 2 # ← deterministic doubling, no jitter ``` The backoff doubles determinist...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: fix(lora): _load_lora_config retry uses deterministic backoff without jitter — thundering herd risk ## Summary [Quorum](https://github.com/KaustubhUp025/quorum) detected a coordination anti-pattern in PR #34981 while re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ined overload — a classic [thundering herd](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/). ## Suggested fix Add full jitter (AWS Builders' Library recommendation): ```python import random ti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
