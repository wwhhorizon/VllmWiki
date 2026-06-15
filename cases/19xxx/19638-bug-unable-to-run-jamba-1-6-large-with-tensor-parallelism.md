# vllm-project/vllm#19638: [Bug]: Unable to run Jamba 1.6 Large with Tensor Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#19638](https://github.com/vllm-project/vllm/issues/19638) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run Jamba 1.6 Large with Tensor Parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Jamba Large on 8xH100 and `experts_int8` quantization, Jamba fails to start due to a shared memory issue `vllm serve "hf-100/Jamba-1.6-large-Spellbound-StoryWriter-398B94A-instruct-0.1-chkpt-468" --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.97 --max-model-len 25000 --quantization experts_int8 —tensor-parallel-size 8` Pipeline parallelism works but has very poor performance for my usecase. ``` ERROR 06-14 04:34:09 [engine.py:458] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/experts_int8.py", line 135, in apply [357/1788] ERROR 06-14 04:34:09 [engine.py:458] return fused_experts( ERROR 06-14 04:34:09 [engine.py:458] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 1186, in fused_experts ERROR 06-14 04:34:09 [engine.py:458] return dispatch_fused_experts_func(inplace)( ERROR 06-14 04:34:09 [engine.py:458] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 1125, in torch_vllm_inplace_fused_experts ERROR 06-14 04:34:09 [engine.py:458] torch.op...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .py:458] File "/home/ubuntu/.local/lib/python3.10/site-packages/triton/compiler/compiler.py", line 413, in __getattribute__ ERROR 06-14 04:34:09 [engine.py:458] self._init_handles() E
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Unable to run Jamba 1.6 Large with Tensor Parallelism bug;stale ### Your current environment ### 🐛 Describe the bug When running Jamba Large on 8xH100 and `experts_int8` quantization, Jamba fails to start due to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: .py:458] return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) ERROR 06-14 04:34:09 [engine.py:458] File "/home/ubuntu/.local/lib/python3.10/site-packages/triton/runtime
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ment ### 🐛 Describe the bug When running Jamba Large on 8xH100 and `experts_int8` quantization, Jamba fails to start due to a shared memory issue `vllm serve "hf-100/Jamba-1.6-large-Spellbound-StoryWriter-398B94A-instru...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ERROR 06-14 04:34:09 [engine.py:458] return dispatch_fused_experts_func(inplace)( ERROR 06-14 04:34:09 [engine.py:458] File "/home/ubun

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
