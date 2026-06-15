# vllm-project/vllm#28517: [Bug]:  ValueError: There is no module or parameter named 'mlp_AR' in TransformersForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#28517](https://github.com/vllm-project/vllm/issues/28517) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;gemm;operator |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  ValueError: There is no module or parameter named 'mlp_AR' in TransformersForCausalLM

### Issue 正文摘录

### Your current environment error when using PaddleOCR-VL ``` vllm serve PaddlePaddle/PaddleOCR-VL \ --trust-remote-code \ --max-num-batched-tokens 16384 \ --no-enable-prefix-caching \ --mm-processor-cache-gb 0 ``` ### 🐛 Describe the bug (EngineCore_DP0 pid=560891) INFO 11-12 13:42:16 [transformers.py:442] Using Transformers backend. (EngineCore_DP0 pid=560891) `torch_dtype` is deprecated! Use `dtype` instead! (EngineCore_DP0 pid=560891) INFO 11-12 13:42:17 [cuda.py:366] Using Flash Attention backend on V1 engine. Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00 (APIServer pid=560804) sys.exit(main()) (APIServer pid=560804) ^^^^^^ (APIServer pid=560804) File "/mnt/sdb/zjh/ARPO/submit/ppocr/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=560804) args.dispatch_function(args) (APIServer pid=560804) File "/mnt/sdb/zjh/ARPO/submit/ppocr/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 57, in cmd (APIServer pid=560804) uvloop.run(run_server(args)) (APIServer pid=560804) File "/mnt/sdb/zjh/ARPO/submit/ppocr/.venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run (APIServer pid=560804...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: pid=560891) INFO 11-12 13:42:16 [transformers.py:442] Using Transformers backend. (EngineCore_DP0 pid=560891) `torch_dtype` is deprecated! Use `dtype` instead! (EngineCore_DP0 pid=560891) INFO 11-12 13:42:17 [cuda.py:36...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: op/__init__.py", line 96, in run (APIServer pid=560804) return __asyncio.run( (APIServer pid=560804) ^^^^^^^^^^^^^^ (APIServer pid=560804) File "/home/suser/.local/share/uv/python/cpython-3.12.11-linux-x86_64-gnu/lib/py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d! Use `dtype` instead! (EngineCore_DP0 pid=560891) INFO 11-12 13:42:17 [cuda.py:366] Using Flash Attention backend on V1 engine. Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00 (APIServer pid=560804) s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: om_engine_args (APIServer pid=560804) async_llm = AsyncLLM.from_vllm_config( (APIServer pid=560804) ^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=560804) File "/mnt/sdb/zjh/ARPO/submit/ppocr/.venv/lib/python3.12/site-packag...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s.py:442] Using Transformers backend. (EngineCore_DP0 pid=560891) `torch_dtype` is deprecated! Use `dtype` instead! (EngineCore_DP0 pid=560891) INFO 11-12 13:42:17 [cuda.py:366] Using Flash Attention backend on V1 engin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
