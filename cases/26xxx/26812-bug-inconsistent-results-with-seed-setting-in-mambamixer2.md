# vllm-project/vllm#26812: [Bug]: Inconsistent Results with Seed Setting in MambaMixer2

| 字段 | 值 |
| --- | --- |
| Issue | [#26812](https://github.com/vllm-project/vllm/issues/26812) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent Results with Seed Setting in MambaMixer2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Despite setting a seed (seed=42) in the script, the results are still not reproducible in a stable manner. After running the code, the outputs from vLLM MambaMixer2 differ significantly on each execution, even though the environment setup, model files, and other parameters remain constant. [Test script](https://gist.github.com/XuanofXXX/cd58fecfb1a077619f298cfeeec4a628) about reproducing the inconsistent result. Error messages: ``` INFO 10-14 22:09:48 [parallel_state.py:1208] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0 y1: tensor([[[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]]], device='cuda:0', dtype=torch.bfloat16) y2: tensor([[[-0.0234, 0.1328, -0.2090], [ 0.5391, 0.1357, -0.2002], [-0.1875, -0.0513, -0.0018]]], device='cuda:0', dtype=torch.bfloat16) {'device': 'cuda', 'dtype': 'bfloat16', 'same': False, 'max_abs_diff': 1.8671875} ``` Besides, I made a [pull request](https://github.com/vllm-project/vllm/pull/26805) that addresses this issue. If there's anything I should be aware of, I would appreciate your feedback. ### Before submitting a new issue... - [x] Make sure you already searched for r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: setting a seed (seed=42) in the script, the results are still not reproducible in a stable manner. After running the code, the outputs from vLLM MambaMixer2 differ significantly on each execution, even though the enviro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ., 0.], [0., 0., 0.], [0., 0., 0.]]], device='cuda:0', dtype=torch.bfloat16) y2: tensor([[[-0.0234, 0.1328, -0.2090], [ 0.5391, 0.1357, -0.2002], [-0.1875, -0.0513, -0.0018]]], device='cuda:0', dtype=torch.bfloat16) {'d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Inconsistent Results with Seed Setting in MambaMixer2 bug;stale ### Your current environment ### 🐛 Describe the bug Despite setting a seed (seed=42) in the script, the results are still not reproducible in a stab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ([[[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]]], device='cuda:0', dtype=torch.bfloat16) y2: tensor([[[-0.0234, 0.1328, -0.2090], [ 0.5391, 0.1357, -0.2002], [-0.1875, -0.0513, -0.0018]]], device='cuda:0', dtype=torch.bflo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _support;moe;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
