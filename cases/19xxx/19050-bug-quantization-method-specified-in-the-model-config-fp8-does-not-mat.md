# vllm-project/vllm#19050: [Bug]: Quantization method specified in the model config (fp8) does not match the quantization method specified in the `quantization` argument (gguf).

| 字段 | 值 |
| --- | --- |
| Issue | [#19050](https://github.com/vllm-project/vllm/issues/19050) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Quantization method specified in the model config (fp8) does not match the quantization method specified in the `quantization` argument (gguf).

### Issue 正文摘录

### Your current environment MODEL_PATH="/data2/jcxy/llm_model/DeepSeek-R1-0528-GGUF-UD-IQ2_XXS/DeepSeek-R1-0528-UD-IQ2_XXS-00001-of-00005.gguf" LOG_FILE="vllm.log" export VLLM_USE_V1=0 SERVED_MODEL_NAME="DeepSeek-R1-0528" export CUDA_VISIBLE_DEVICES=2,3,4,5 # 运行命令 nohup vllm serve \ "$MODEL_PATH" \ --hf-config-path /data2/jcxy/llm_model/DeepSeek-R1-0528-GGUF-UD-IQ2_XXS \ --tokenizer /data2/jcxy/llm_model/DeepSeek-R1-0528-GGUF-UD-IQ2_XXS \ --served-model-name "$SERVED_MODEL_NAME" \ --trust-remote-code \ --port 6011 \ --host 0.0.0.0 \ --dtype auto \ --max-model-len 8192 \ --gpu_memory_utilization 0.98 \ --tensor_parallel_size 4 \ --enable-prefix-caching \ >"$LOG_FILE" 2>&1 & --------------------------------------- ### 🐛 Describe the bug INFO 06-03 11:53:19 [__init__.py:243] Automatically detected platform cuda. INFO 06-03 11:53:22 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-03 11:53:22 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 06-03 11:53:22 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. INFO 06-03 11:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Quantization method specified in the model config (fp8) does not match the quantization method specified in the `quantization` argument (gguf). bug;stale ### Your current environment MODEL_PATH="/data2/jcxy/llm_m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Quantization method specified in the model config (fp8) does not match the quantization method specified in the `quantization` argument (gguf). bug;stale ### Your current environment MODEL_PATH="/data2/jcxy/llm_m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Quantization method specified in the model config (fp8) does not match the quantization method specified in the `quantization` argument (gguf). bug;stale ### Your current environment MODEL_PATH="/data2/jcxy/llm_m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m.log" export VLLM_USE_V1=0 SERVED_MODEL_NAME="DeepSeek-R1-0528" export CUDA_VISIBLE_DEVICES=2,3,4,5 # 运行命令 nohup vllm serve \ "$MODEL_PATH" \ --hf-config-path /data2/jcxy/llm_model/DeepSeek-R1-0528-GGUF-UD-IQ2_XXS \ --...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0/site-packages/vllm/entrypoints/cli/main.py", line 56, in main args.dispatch_function(args) File "/data/jcxy/haolu/anaconda3/envs/haolu/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 42, in cmd uvloo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
