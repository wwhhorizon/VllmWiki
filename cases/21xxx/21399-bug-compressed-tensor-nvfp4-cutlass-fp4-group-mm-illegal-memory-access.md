# vllm-project/vllm#21399: [Bug]: Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access

| 字段 | 值 |
| --- | --- |
| Issue | [#21399](https://github.com/vllm-project/vllm/issues/21399) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;kernel;moe;operator;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In main branch `lm_eval --model vllm --model_args "pretrained=nm-testing/Qwen3-30B-A3B-NVFP4,max_model_len=32768" --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto` ```bash File "/home/wentao/vllm-source/vllm/compilation/cuda_piecewise_backend.py", line 156, in __call__ return entry.runnable(*args) ^^^^^^^^^^^^^^^^^^^^^ File "/home/wentao/vllm-source/vllm/compilation/compiler_interface.py", line 512, in compiled_graph graph_output = inductor_compiled_graph(list_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/wentao/.wentao_env/lib/python3.12/site-packages/torch/_inductor/output_code.py", line 460, in __call__ return self.current_callable(inputs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/wentao/.cache/vllm/torch_compile_cache/80c2bd6cc7/rank_0_0/inductor_cache/qt/cqtz3w2ca75u6xjwst4c3mg557dp4fir43hj4vyy5qmlehv3vb3k.py", line 644, in call buf14 = torch.ops.vllm.moe_forward.default(buf12, buf13, 'model.layers.24.mlp.experts') ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/wentao/.wentao_env/lib/python3.12/site-packages/torch/_ops.py", line 756, in __call__ return se...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ^^^^^^^^^^^^^^^^^^^^^ File "/home/wentao/vllm-source/vllm/compilation/compiler_interface.py", line 512, in compiled_graph graph_output = inductor_compiled_graph(list_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access bug ### Your current environment ### 🐛 Describe the bug In main branch `lm_eval --model vllm --model_args "pretrained=nm-testing/Qwen3-30B-A3B-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ir43hj4vyy5qmlehv3vb3k.py", line 644, in call buf14 = torch.ops.vllm.moe_forward.default(buf12, buf13, 'model.layers.24.mlp.experts') ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: wen3-30B-A3B-NVFP4,max_model_len=32768" --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto` ```bash File "/home/wentao/vllm-source/vllm/compilation/cuda_piecewise_backend.py", line 156, in __call__ retu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access bug ### Your current environment ### 🐛 Describe the bug In main branch `lm_eval --model vllm --model_args "pretrained=nm-testing/Qwen3-30B-A3B-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
