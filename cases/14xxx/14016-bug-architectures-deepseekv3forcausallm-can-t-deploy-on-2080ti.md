# vllm-project/vllm#14016: [Bug]: Architectures DeepseekV3ForCausalLM can't deploy on 2080ti

| 字段 | 值 |
| --- | --- |
| Issue | [#14016](https://github.com/vllm-project/vllm/issues/14016) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Architectures DeepseekV3ForCausalLM can't deploy on 2080ti

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model /mnt/e/Code/models/Moonlight-16B-A3B-Instruct --max-model-len 8192 --max-num-seqs=3 --dtype=half --swap_space=0 --gpu-memory-utilization 0.75 --served-model-name vLLM/Moonlight-16B-A3B-Instruct --tensor-parallel-size 2 --no-enable-prefix-caching --trust-remote-code ``` (base) root@DESKTOP-PEPA2G9:~# python3 -m vllm.entrypoints.openai.api_server --model /mnt/e/Code/models/Moonlight-16B-A3B-Instruct --max-model-len 8192 --max-num-seqs=3 --dtype=half --swap_space=0 --gpu-memory-utilization 0.75 --served-model-name vLLM/Moonlight-16B-A3B-Instruct --tensor-parallel-size 2 --no-enable-prefix-caching --trust-remote-code INFO 02-28 12:52:30 __init__.py:207] Automatically detected platform cuda. INFO 02-28 12:52:30 api_server.py:912] vLLM API server version 0.7.3 INFO 02-28 12:52:30 api_server.py:913] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: [Bug]: Architectures DeepseekV3ForCausalLM can't deploy on 2080ti bug;stale ### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model /mnt/e/Code/models/Moonlight-16B-A3B-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed platform cuda. INFO 02-28 12:52:30 api_server.py:912] vLLM API server version 0.7.3 INFO 02-28 12:52:30 api_server.py:913] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: odels/Moonlight-16B-A3B-Instruct --max-model-len 8192 --max-num-seqs=3 --dtype=half --swap_space=0 --gpu-memory-utilization 0.75 --served-model-name vLLM/Moonlight-16B-A3B-Instruct --tensor-parallel-size 2 --no-enable-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Architectures DeepseekV3ForCausalLM can't deploy on 2080ti bug;stale ### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model /mnt/e/Code/models/Moonlight-16B-A3B-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
