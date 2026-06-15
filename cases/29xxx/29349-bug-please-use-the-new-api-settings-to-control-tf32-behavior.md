# vllm-project/vllm#29349: [Bug]: Please use the new API settings to control TF32 behavior...

| 字段 | 值 |
| --- | --- |
| Issue | [#29349](https://github.com/vllm-project/vllm/issues/29349) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Please use the new API settings to control TF32 behavior...

### Issue 正文摘录

### Your current environment I'm using docker btw... this is the host (yes it has vllm but it doesn't work - I know the issue has been fixed in v0.11.1) That's the host but I generally use docker so the above info is kinda irrelevant appart from hardware info. On host I have `v0.11.0` which I know doesn't work (because of [the above issue I mentioned](https://gist.github.com/wasertech/fd579f5b09b2e9e0206dc5dac092791b#file-vllm-err-graph-txt)) so I tried `v0.11.2` and the nightly build `0.11.2.dev201+g55c21c883`; both failed with the same error. ### 🐛 Describe the bug It seems related to this warning but it's unclear to me which library should address it (probably `transformers`) but since it happens inside the vllm docker image, it's an issue for vllm either way. ``` UserWarning: Please use the new API settings to control TF32 behavior, such as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.allow_tf32 = True, torch.backends.cudnn.allow_tf32 = True, allowTF32CuDNN() and allowTF32CuBLAS() will be deprecated after Pytorch 2.9. Please see https://pytorch.org/docs/main/notes/cuda.htm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: to control TF32 behavior... bug ### Your current environment I'm using docker btw... this is the host (yes it has vllm but it doesn't work - I know the issue has been fixed in v0.11.1) That's the host but I generally us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: h as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.allow_tf32 = True, torch.backends.cudnn.allow_tf32 = True, allo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Please use the new API settings to control TF32 behavior, such as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.al...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n answer lots of frequently asked questions. EDIT: Created a ticket on `hf/transformers` correctness ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;sampli...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ettings to control TF32 behavior, such as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.allow_tf32 = True, torch.b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
