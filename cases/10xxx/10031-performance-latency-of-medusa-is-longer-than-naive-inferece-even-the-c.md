# vllm-project/vllm#10031: [Performance]: latency of medusa is longer than naive inferece even the concurreny =2

| 字段 | 值 |
| --- | --- |
| Issue | [#10031](https://github.com/vllm-project/vllm/issues/10031) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: latency of medusa is longer than naive inferece even the concurreny =2

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I compared the performance of the Medusa method and the naive method on a dataset containing 100 prompts and found that even when the concurrency was set to 2, the performance of the Medusa method was worse than that of naive inference. The detailed results (average) are shown in below, the draft acceptance rate is around 50% (reported by the vllm log), I understand that Medusa's performance may be affected when the concurrency is high, however, the performance drop is too significant. hardware: single A100 40GB model: Qwen2-1.5B deploy script: `export CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/model/Qwen2-1.5B-Instruct \ --host 0.0.0.0 \ --trust-remote-code \ --max-model-len 32768 \ --port=7802 \ --disable-log-requests \ --tensor-parallel-size 1 \ --speculative-model /mnt/model/exp2_Qwen2_Medusa_3_head_32_weight_2_4096/_medusa_mlp_Qwen2-1.5B-Instruct_medusa_3_lr_0.0001_layers_2/converted \ --speculative-draft-tensor-parallel-size 1 \ --num-speculative-tokens 1 \ --use-v2-block-manager \` | Concurrency | Naive(s) | Medusa(s) | |----------|----------|----------| | 1 | 785 | 577 | | 2 | 335 | 367 | |...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: medusa is longer than naive inferece even the concurreny =2 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I compared the performance of the Medusa method and th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: igh, however, the performance drop is too significant. hardware: single A100 40GB model: Qwen2-1.5B deploy script: `export CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/model/Qwen2-1.5B-Instruct \ --host 0.0.0.0 \ --trust-remo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: latency of medusa is longer than naive inferece even the concurreny =2 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I compared the performance o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: er, the performance drop is too significant. hardware: single A100 40GB model: Qwen2-1.5B deploy script: `export CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/model/Qwen2-1.5B-Instruct \ --host 0.0.0.0 \ --trust-remote-code \...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t-tensor-parallel-size 1 \ --num-speculative-tokens 1 \ --use-v2-block-manager \` | Concurrency | Naive(s) | Medusa(s) | |----------|----------|----------| | 1 | 785 | 577 | | 2 | 335 | 367 | | 3 | 268 | 291 | | 4 | 226...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
