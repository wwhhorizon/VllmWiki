# vllm-project/vllm#32554: [Bug]: Error in inspecting model architecture 'Gemma3ForConditionalGeneration'

| 字段 | 值 |
| --- | --- |
| Issue | [#32554](https://github.com/vllm-project/vllm/issues/32554) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error in inspecting model architecture 'Gemma3ForConditionalGeneration'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hiya! I'm trying to load google/medgemma-4b-it with a cpu-only machine, and vLLM doesn't seem very willing to do so. ``` ERROR 01-18 15:21:03 [registry.py:741] Error in inspecting model architecture 'Gemma3ForConditionalGeneration' ERROR 01-18 15:21:03 [registry.py:741] Traceback (most recent call last): ERROR 01-18 15:21:03 [registry.py:741] File "/home/skullian/gateway/scanhealth/.venv/lib/python3.13/site-packages/vllm/model_executor/models/registry.py", line 1163, in _run_in_subprocess ERROR 01-18 15:21:03 [registry.py:741] returned.check_returncode() ERROR 01-18 15:21:03 [registry.py:741] ~~~~~~~~~~~~~~~~~~~~~~~~~^^ ERROR 01-18 15:21:03 [registry.py:741] File "/home/skullian/.local/share/uv/python/cpython-3.13.11-linux-x86_64-gnu/lib/python3.13/subprocess.py", line 508, in check_returncode ERROR 01-18 15:21:03 [registry.py:741] raise CalledProcessError(self.returncode, self.args, self.stdout, ERROR 01-18 15:21:03 [registry.py:741] self.stderr) ERROR 01-18 15:21:03 [registry.py:741] subprocess.CalledProcessError: Command '['/home/skullian/gateway/scanhealth/.venv/bin/python3', '-m', 'vllm.model_executor.models.registry']' died...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: arning: 'vllm.model_executor.models.registry' found in sys.modules after import of package 'vllm.model_executor.models', but prior to execution of 'vllm.model_executor.models.registry'; this may result in unpredictable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error in inspecting model architecture 'Gemma3ForConditionalGeneration' bug;stale ### Your current environment ### 🐛 Describe the bug Hiya! I'm trying to load google/medgemma-4b-it with a cpu-only machine, and vL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: or in inspecting model architecture 'Gemma3ForConditionalGeneration' bug;stale ### Your current environment ### 🐛 Describe the bug Hiya! I'm trying to load google/medgemma-4b-it with a cpu-only machine, and vLLM doesn't...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: AsyncEngineArgs( model=self.model_name, dtype="bfloat16", max_model_len=max_len, max_num_seqs=max_seqs, tensor_parallel_size=self.reserve_size, enable_chunked_prefill=True, enable_
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ON}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_x86_64.whl --torch-backend cpu` Seems to work fine with the GPU binaries Hope you can help! Let me know if there's anything I'm missing. ### Before submitting a new...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
