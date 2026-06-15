# vllm-project/vllm#37367: [Bug]: gcc: internal compiler error: Segmentation fault signal terminated program cc1

| 字段 | 值 |
| --- | --- |
| Issue | [#37367](https://github.com/vllm-project/vllm/issues/37367) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gcc: internal compiler error: Segmentation fault signal terminated program cc1

### Issue 正文摘录

### Your current environment rtx 3090 * 2 cuda version:12.9 Driver Version 575.51.03 CentOS Linux 8 docker image: vllm/vllm-openai:v0.17.1 ### 🐛 Describe the bug docker run --name $SERVICE_NAME -d --gpus all --shm-size 30.24gb --network host \ -v $WORKSPACE_PATH:/vllm-workspace vllm/vllm-openai:v0.17.1 以上脚本启动容器时，容器中的启动脚本为 #!/bin/bash export CUDA_VISIBLE_DEVICES=0 vllm serve ./PaddleOCR-VL --config llm_config.yaml 报错 (APIServer pid=7) INFO 03-17 11:10:14 [utils.py:238] non-default args: {'model_tag': './PaddleOCR-VL', 'host': '0.0.0.0', 'port': 18023, 'model': './PaddleOCR-VL', 'trust_remote_code': True, 'served_model_name': ['PaddleOCR-VL-0.9B'], 'gpu_memory_utilization': 0.3, 'enable_prefix_caching': False, 'mm_processor_cache_gb': 0.0} (APIServer pid=7) WARNING 03-17 11:10:14 [envs.py:1710] Unknown vLLM environment variable detected: VLLM_DISABLE_TRITON (APIServer pid=7) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=7) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=7) INFO 03-17 11:10:14 [model.py:531] Resolved architecture: PaddleOCRVL...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: [envs.py:1710] Unknown vLLM environment variable detected: VLLM_DISABLE_TRITON (APIServer pid=7) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=7)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: gcc: internal compiler error: Segmentation fault signal terminated program cc1 bug ### Your current environment rtx 3090 * 2 cuda version:12.9 Driver Version 575.51.03 CentOS Linux 8 docker image: vllm/vllm-opena...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: #!/bin/bash export CUDA_VISIBLE_DEVICES=0 vllm serve ./PaddleOCR-VL --config llm_config.yaml 报错 (APIServer pid=7) INFO 03-17 11:10:14 [utils.py:238] non-default args: {'model_tag': './PaddleOCR-VL', 'host': '0.0.0.0', '...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: on fault signal terminated program cc1 bug ### Your current environment rtx 3090 * 2 cuda version:12.9 Driver Version 575.51.03 CentOS Linux 8 docker image: vllm/vllm-openai:v0.17.1 ### 🐛 Describe the bug docker run --n...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
