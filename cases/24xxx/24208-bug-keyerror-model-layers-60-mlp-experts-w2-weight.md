# vllm-project/vllm#24208: [Bug]: KeyError: 'model.layers.60.mlp.experts.w2_weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#24208](https://github.com/vllm-project/vllm/issues/24208) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'model.layers.60.mlp.experts.w2_weight'

### Issue 正文摘录

### Your current environment ```text vllm==0.9.2 transformers==4.53.0 ``` ### 🐛 Describe the bug ```shell vllm serve /data/model/DeepSeek-V3___1-AWQ --trust-remote-code \ --dtype float16 \ --max-model-len 32658 \ --max-seq-len-to-capture 32658 -tp 8 \ --gpu-memory-utilization 0.98 \ --max-num-seqs 128 \ --block-size 64 ``` with error: And I tried another command: ```shell vllm serve /data/model/tclf90/DeepSeek-V3___1-AWQ --trust-remote-code \ --dtype float16 \ --max-model-len 32658 \ --max-seq-len-to-capture 32658 -tp 8 \ --gpu-memory-utilization 0.98 \ --max-num-seqs 128 \ --block-size 64 \ --quantization awq ``` Still the same error: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: hell vllm serve /data/model/DeepSeek-V3___1-AWQ --trust-remote-code \ --dtype float16 \ --max-model-len 32658 \ --max-seq-len-to-capture 32658 -tp 8 \ --gpu-memory-utilization 0.98 \ --max-num-seqs 128 \ --block-size 64...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: : ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: re 32658 -tp 8 \ --gpu-memory-utilization 0.98 \ --max-num-seqs 128 \ --block-size 64 ``` with error: And I tried another command: ```shell vllm serve /data/model/tclf90/DeepSeek-V3___1-AWQ --trust-remote-code \ --dtype...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: KeyError: 'model.layers.60.mlp.experts.w2_weight' bug ### Your current environment ```text vllm==0.9.2 transformers==4.53.0 ``` ### 🐛 Describe the bug ```shell vllm serve /data/model/DeepSeek-V3___1-AWQ --trust-r...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: KeyError: 'model.layers.60.mlp.experts.w2_weight' bug ### Your current environment ```text vllm==0.9.2 transformers==4.53.0 ``` ### 🐛 Describe the bug ```shell vllm serve /data/model/DeepSeek-V3___1-AWQ --trust-r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
