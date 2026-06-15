# vllm-project/vllm#14814: [Bug]: Gemma-3-27b-it-GPTQ Can't run in sm75, vllm-0.7.4.dev

| 字段 | 值 |
| --- | --- |
| Issue | [#14814](https://github.com/vllm-project/vllm/issues/14814) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-3-27b-it-GPTQ Can't run in sm75, vllm-0.7.4.dev

### Issue 正文摘录

### Your current environment ``` (base) root@DESKTOP-PEPA2G9:/mnt/c/Users/IAdmin# pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly Successfully installed compressed-tensors-0.9.2 python-json-logger-3.3.0 ray-2.43.0 scipy-1.15.2 vllm-0.7.4.dev439+gc77620d2 xgrammar-0.1.15 (base) root@DESKTOP-PEPA2G9:/mnt/c/Users/IAdmin# pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3 Successfully installed transformers-4.50.0.dev0 ``` ### 🐛 Describe the bug After installing the latest vllm and transformers as instructed here, I am unable to run the gemma3 model: https://huggingface.co/ISTA-DASLab/gemma-3-27b-it-GPTQ-4b-128g ``` (base) root@DESKTOP-PEPA2G9:/mnt/c/Users/IAdmin# python3 -m vllm.entrypoints.openai.api_server --model /mnt/e/Code/models/gemma-3-27b-it-GPTQ-4b-128g --max-model-len 8192 --max-num-seqs=3 --dtype=half --swap_space=0 --gpu-memory-utilization 0.65 --served-model-name vLLM/gemma-3-27b-it-GPTQ-4b-128g --tensor-parallel-size 2 --no-enable-prefix-caching INFO 03-14 17:59:58 [__init__.py:256] Automatically detected platform cuda. INFO 03-14 17:59:59 [api_server.py:912] vLLM API server version 0.7.4.dev439+gc77620d2 INFO 03-14 17:59...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/e/Code/models/gemma-3-27b-it-GP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ent environment ``` (base) root@DESKTOP-PEPA2G9:/mnt/c/Users/IAdmin# pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly Successfully installed compressed-tensors-0.9.2 python-json-logger-3.3.0 ray-2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma-3-27b-it-GPTQ Can't run in sm75, vllm-0.7.4.dev bug ### Your current environment ``` (base) root@DESKTOP-PEPA2G9:/mnt/c/Users/IAdmin# pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: dels/gemma-3-27b-it-GPTQ-4b-128g --max-model-len 8192 --max-num-seqs=3 --dtype=half --swap_space=0 --gpu-memory-utilization 0.65 --served-model-name vLLM/gemma-3-27b-it-GPTQ-4b-128g --tensor-parallel-size 2 --no-enable-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Gemma-3-27b-it-GPTQ Can't run in sm75, vllm-0.7.4.dev bug ### Your current environment ``` (base) root@DESKTOP-PEPA2G9:/mnt/c/Users/IAdmin# pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
