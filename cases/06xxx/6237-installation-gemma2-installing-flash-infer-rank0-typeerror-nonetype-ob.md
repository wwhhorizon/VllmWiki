# vllm-project/vllm#6237: [Installation]: Gemma2 Installing Flash Infer `[rank0]: TypeError: 'NoneType' object is not callable`

| 字段 | 值 |
| --- | --- |
| Issue | [#6237](https://github.com/vllm-project/vllm/issues/6237) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Gemma2 Installing Flash Infer `[rank0]: TypeError: 'NoneType' object is not callable`

### Issue 正文摘录

The source of your error is that you have installed the wrong version of FlashInfer. FlashInfer builds wheels for specific torch and cuda versions. vLLM v0.5.1 uses `torch==2.3` and `cuda==12.1`. So you will likely want to download the following wheel: ```bash pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.3 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: Gemma2 Installing Flash Infer `[rank0]: TypeError: 'NoneType' object is not callable` installation The source of your error is that you have installed the wrong version of FlashInfer. FlashInfer builds wh
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: The source of your error is that you have installed the wrong version of FlashInfer. FlashInfer builds wheels for specific torch and cuda versions. vLLM v0.5.1 uses `torch==2.3` and `cuda==12.1`. So you will likely want...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: version of FlashInfer. FlashInfer builds wheels for specific torch and cuda versions. vLLM v0.5.1 uses `torch==2.3` and `cuda==12.1`. So you will likely want to download the following wheel: ```bash pip install flashinf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Installation]: Gemma2 Installing Flash Infer `[rank0]: TypeError: 'NoneType' object is not callable` installation The source of your error is that you have installed the wrong version of FlashInfer. FlashInfer builds w...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Installation]: Gemma2 Installing Flash Infer `[rank0]: TypeError: 'NoneType' object is not callable` installation The source of your error is that you have installed the wrong version of FlashInfer. FlashInfer builds w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
