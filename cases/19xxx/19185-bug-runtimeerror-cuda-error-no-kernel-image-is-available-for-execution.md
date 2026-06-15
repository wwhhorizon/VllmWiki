# vllm-project/vllm#19185: [Bug]:  RuntimeError: CUDA error: no kernel image is available for execution on the device with nvidia v100

| 字段 | 值 |
| --- | --- |
| Issue | [#19185](https://github.com/vllm-project/vllm/issues/19185) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  RuntimeError: CUDA error: no kernel image is available for execution on the device with nvidia v100

### Issue 正文摘录

### Your current environment git commit is c56ed8bb0e0e335033797044e33acc2b00e06b79 DOCKER_BUILDKIT=1 sudo docker build . --target vllm-openai \ --tag myvllm --file docker/Dockerfile \ --build-arg max_jobs=4 \ --build-arg nvcc_threads=1 \ --build-arg torch_cuda_arch_list="7.0" \ --build-arg RUN_WHEEL_CHECK=false ### 🐛 Describe the bug docker run --runtime nvidia --gpus '"device=1,2"' --rm \ -v /data/modelscope:/root/.cache/modelscope \ -e VLLM_USE_MODELSCOPE=True \ -p 11435:8000 --ipc=host myvllm \ --model Qwen/Qwen3-0.6B-GPTQ-Int8 \ --max-model-len 8192 --served-model-name qt-vllm INFO 06-04 22:38:00 [__init__.py:244] Automatically detected platform cuda. INFO 06-04 22:38:05 [api_server.py:1289] vLLM API server version 0.9.1.dev180+gc56ed8bb0.d20250605 INFO 06-04 22:38:05 [cli_args.py:309] non-default args: {'model': 'Qwen/Qwen3-0.6B-GPTQ-Int8', 'max_model_len': 8192, 'served_model_name': ['qt-vllm']} 2025-06-04 22:38:07,106 - modelscope - WARNING - Using branch: master as version is unstable, use with caution 2025-06-04 22:38:07,321 - modelscope - INFO - Target directory already exists, skipping creation. 2025-06-04 22:38:08,150 - modelscope - WARNING - Using branch: master as v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rent environment git commit is c56ed8bb0e0e335033797044e33acc2b00e06b79 DOCKER_BUILDKIT=1 sudo docker build . --target vllm-openai \ --tag myvllm --file docker/Dockerfile \ --build-arg max_jobs=4 \ --build-arg nvcc_thre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device with nvidia v100 bug;stale ### Your current environment git commit is c56ed8bb0e0e335033797044e33acc2b00e06b79 DOCKER_BUILDKIT=1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ug docker run --runtime nvidia --gpus '"device=1,2"' --rm \ -v /data/modelscope:/root/.cache/modelscope \ -e VLLM_USE_MODELSCOPE=True \ -p 11435:8000 --ipc=host myvllm \ --model Qwen/Qwen3-0.6B-GPTQ-Int8 \ --max-model-l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s 7.5. warnings.warn( WARNING 06-04 22:38:22 [config.py:930] gptq quantization is not fully optimized yet. The speed can be slower than non-quantized models. WARNING 06-04 22:38:22 [arg_utils.py:1633] Compute Capability...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: --build-arg torch_cuda_arch_list="7.0" \ --build-arg RUN_WHEEL_CHECK=false ### 🐛 Describe the bug docker run --runtime nvidia --gpus '"device=1,2"' --rm \ -v /data/modelscope:/root/.cache/modelscope \ -e VLLM_USE_MODELS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
