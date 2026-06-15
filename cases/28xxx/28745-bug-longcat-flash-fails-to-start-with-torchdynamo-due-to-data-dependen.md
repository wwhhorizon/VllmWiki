# vllm-project/vllm#28745: [Bug]: LongCat-Flash fails to start with TorchDynamo due to “Data-dependent assertion failed” in FusedMoE

| 字段 | 值 |
| --- | --- |
| Issue | [#28745](https://github.com/vllm-project/vllm/issues/28745) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | fp8;moe |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LongCat-Flash fails to start with TorchDynamo due to “Data-dependent assertion failed” in FusedMoE

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve meituan-longcat/LongCat-Flash-Chat-FP8 \ --trust-remote-code \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --max-model-len 32768 \ --max-num-seqs 4 goes to this error https://paste.ubuntu.com/p/ZBjQdRx9v6/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#28891 [MoE Refactor][5/N] Isolate zero expert to LongCatFlash

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### 🐛 Describe the bug vllm serve meituan-longcat/LongCat-Flash-Chat-FP8 \ --trust-remote-code \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --max-model-len 32768 \ --max-num-seqs 4 goes to this error https://...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: start with TorchDynamo due to “Data-dependent assertion failed” in FusedMoE bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve meituan-longcat/LongCat-Flash-Chat-FP8 \ --trust-remote-code \ --enabl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: v6/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: code \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --max-model-len 32768 \ --max-num-seqs 4 goes to this error https://paste.ubuntu.com/p/ZBjQdRx9v6/ ### Before submitting a new issue... - [x] Make sure you al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ith TorchDynamo due to “Data-dependent assertion failed” in FusedMoE bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve meituan-longcat/LongCat-Flash-Chat-FP8 \ --trust-remote-code \ --enable-exper...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28891](https://github.com/vllm-project/vllm/pull/28891) | mentioned | 0.6 | [MoE Refactor][5/N] Isolate zero expert to LongCatFlash | Refactor][5/N] Isolate zero expert to LongCatFlash ## Purpose #28152 #28745 Fix dimension mismatch error in LongCat Flash MoE model when using zero experts. The issue occurred whe… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
