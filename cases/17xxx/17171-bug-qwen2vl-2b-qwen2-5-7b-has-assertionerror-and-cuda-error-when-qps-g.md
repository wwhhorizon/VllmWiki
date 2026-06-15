# vllm-project/vllm#17171: [Bug]: Qwen2VL-2b / Qwen2.5-7b has AssertionError and Cuda error when qps goes higher

| 字段 | 值 |
| --- | --- |
| Issue | [#17171](https://github.com/vllm-project/vllm/issues/17171) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;kernel;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2VL-2b / Qwen2.5-7b has AssertionError and Cuda error when qps goes higher

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The model Qwen2VL-2b can be successfully deployed, and the output is normal when I sent request 1 by 1. But when I increase the qps to 3 or even more, the assertion error `assert query.shape[0] == num_prefill_query_tokens` appears. After a few seconds, new error `RuntimeError: CUDA error: an illegal memory access was encountered` appears and the model can't process any request. AssertionError 1 `File "/home/hzh/aigcqwen2vl2bvllm/bin/qwen2vl2b/model/qwen2vl2b_infer_engine.py", line 122, in get_qwen2vl2b_res outputs = self.model.generate([llm_inputs], sampling_params=sampling_params) File "/home/hzh/aigcqwen2vl2bvllm/bin/des/python_env/lib/python3.10/site-packages/vllm/utils.py", line 1134, in inner return fn(*args, **kwargs) File "/home/hzh/aigcqwen2vl2bvllm/bin/des/python_env/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 470, in generate outputs = self._run_engine(use_tqdm=use_tqdm) File "/home/hzh/aigcqwen2vl2bvllm/bin/des/python_env/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1409, in _run_engine step_outputs = self.llm_engine.step() File "/home/hzh/aigcqwen2vl2bvllm/bin/des/python_env/lib/python3....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: l_runner.py", line 1228, in _prepare_model_input_tensors return self.builder.build() # type: ignore File "/home/hzh/aigcqwen2vl2bvllm/bin/des/python_env/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 89...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: / Qwen2.5-7b has AssertionError and Cuda error when qps goes higher bug;stale ### Your current environment ### 🐛 Describe the bug The model Qwen2VL-2b can be successfully deployed, and the output is normal when I sent r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen2VL-2b / Qwen2.5-7b has AssertionError and Cuda error when qps goes higher bug;stale ### Your current environment ### 🐛 Describe the bug The model Qwen2VL-2b can be successfully deployed, and the output is no...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2vl2bvllm/bin/des/python_env/lib/python3.10/site-packages/vllm/attention/backends/flash_attn.py", line 775, in forward assert query.shape[0] == num_prefill_query_tokens AssertionError ]` AssetionError2 `File "/home/hzh/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2VL-2b / Qwen2.5-7b has AssertionError and Cuda error when qps goes higher bug;stale ### Your current environment ### 🐛 Describe the bug The model Qwen2VL-2b can be successfully deployed, and the output is no...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
