# vllm-project/vllm#34504: [Bug]: GLM-5-FP8 Crash - Engine core initialization failed

| 字段 | 值 |
| --- | --- |
| Issue | [#34504](https://github.com/vllm-project/vllm/issues/34504) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-5-FP8 Crash - Engine core initialization failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is how i run GLM-5: ```python $ uv run vllm serve zai-org/GLM-5-FP8 --tensor-parallel-size 8 --tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice ``` how i install vllm as per mention [https://github.com/vllm-project/recipes/blob/main/GLM/GLM5.md](url) ```shell export VLLM_COMMIT=ec12d39d44739bee408ec1473acc09e75daf1a5d uv pip install vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/${VLLM_COMMIT} uv pip install git+https://github.com/huggingface/transformers.git ``` there is issue with deep gemm so i run this , reference: [https://github.com/vllm-project/vllm/issues/29946](url) ```shell pip install git+https://github.com/deepseek-ai/DeepGEMM.git@v2.1.1.post3 --no-build-isolation ``` its successfull like call v1/models , but when do completions it crashes. the error: ``` (Worker_TP3 pid=69231) ERROR 02-13 15:54:32 [multiproc_executor.py:863] self._capture_cudagraphs( (Worker_TP3 pid=69231) ERROR 02-13 15:54:32 [multiproc_executor.py:863] ~~~~~~~~~~~~~~~~~~~~~~~~^ (Worker_TP3 pid=69231) ERROR 02-13 15:54:32 [multiproc_executor.py:863] batch_descriptors=batch_descs, (Worker_TP3 pid=6923...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 7 --reasoning-parser glm45 --enable-auto-tool-choice ``` how i install vllm as per mention [https://github.com/vllm-project/recipes/blob/main/GLM/GLM5.md](url) ```shell export VLLM_COMMIT=ec12d39d44739bee408ec1473acc09e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: GLM-5-FP8 Crash - Engine core initialization failed bug ### Your current environment ### 🐛 Describe the bug This is how i run GLM-5: ```python $ uv run vllm serve zai-org/GLM-5-FP8 --tensor-parallel-size 8 --tool...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ec12d39d44739bee408ec1473acc09e75daf1a5d uv pip install vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/${VLLM_COMMIT} uv pip install git+https://github.com/huggingface/transformers.git ``` there is i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: d=69231) ERROR 02-13 15:54:32 [multiproc_executor.py:863] output_block_scale=output_block_scale, (Worker_TP3 pid=69231) ERROR 02-13 15:54:32 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s://wheels.vllm.ai/${VLLM_COMMIT} uv pip install git+https://github.com/huggingface/transformers.git ``` there is issue with deep gemm so i run this , reference: [https://github.com/vllm-project/vllm/issues/29946](url)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
