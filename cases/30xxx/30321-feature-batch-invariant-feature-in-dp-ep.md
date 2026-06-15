# vllm-project/vllm#30321: [Feature]:  Batch Invariant Feature in DP+EP

| 字段 | 值 |
| --- | --- |
| Issue | [#30321](https://github.com/vllm-project/vllm/issues/30321) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Batch Invariant Feature in DP+EP

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I use batch-invariant fuature in > https://github.com/vllm-project/vllm/issues/27433 I try in Qwen/Qwen3-30B-A3B-Instruct-2507 in tp=8,it's worked but when I try use dp+ep to run this model, The results showed inconsistency. ` export VLLM_BATCH_INVARIANT=1 vllm serve $MODEL_PATH --trust-remote-code --block-size 64 --served-model-name qwen3 --max-model-len 8192 --max-num-batched-tokens 8192 --max-num-seqs 32 --gpu-memory-utilization 0.98 --enforce_eager --data-parallel-size 8 --enable-expert-parallel ` However, I also noticed something interesting: when dp=2, the results regained consistency, `export VLLM_BATCH_INVARIANT=1 vllm serve $MODEL_PATH --trust-remote-code --block-size 64 --served-model-name qwen3 --max-model-len 8192 --max-num-batched-tokens 8192 --max-num-seqs 32 --gpu-memory-utilization 0.98 --enforce_eager --data-parallel-size 2 --enable-expert-parallel ` ​This phenomenon makes me wonder if when dp=2, the operation only requires the accumulation of two elements, thus avoiding inconsistency issues, which only arise when dp>2.​​ ​Do you have any advice on this issue？ @yewentao256 ### Alternatives _No response_ ### Additional contex...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ature in > https://github.com/vllm-project/vllm/issues/27433 I try in Qwen/Qwen3-30B-A3B-Instruct-2507 in tp=8,it's worked but when I try use dp+ep to run this model, The results showed inconsistency. ` export VLLM_BATC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Batch Invariant Feature in DP+EP feature request;stale ### 🚀 The feature, motivation and pitch I use batch-invariant fuature in > https://github.com/vllm-project/vllm/issues/27433 I try in Qwen/Qwen3-30B-A3B-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: port VLLM_BATCH_INVARIANT=1 vllm serve $MODEL_PATH --trust-remote-code --block-size 64 --served-model-name qwen3 --max-model-len 8192 --max-num-batched-tokens 8192 --max-num-seqs 32 --gpu-memory-utilization 0.98 --enfor...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: -memory-utilization 0.98 --enforce_eager --data-parallel-size 8 --enable-expert-parallel ` However, I also noticed something interesting: when dp=2, the results regained consistency, `export VLLM_BATCH_INVARIANT=1 vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
