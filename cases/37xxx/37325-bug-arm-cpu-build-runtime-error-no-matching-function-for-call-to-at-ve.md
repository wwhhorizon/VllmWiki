# vllm-project/vllm#37325: [Bug][ARM CPU] Build/Runtime error: no matching function for call to ‘at::vec::CPU_CAPABILITY::VecMask<long int, 4>::VecMask(int&)’ when serving Qwen3-VL-8B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#37325](https://github.com/vllm-project/vllm/issues/37325) |
| 状态 | open |
| 标签 | bug;cpu |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ARM CPU] Build/Runtime error: no matching function for call to ‘at::vec::CPU_CAPABILITY::VecMask<long int, 4>::VecMask(int&)’ when serving Qwen3-VL-8B-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # install ```bash git clone https://github.com/vllm-project/vllm vllm-cpu && \ cd vllm-cpu && \ git checkout main && \ git log -n1 && \ pip3 install --break-system-packages -r requirements/cpu.txt && \ VLLM_TARGET_DEVICE=cpu pip install --break-system-packages . --no-build-isolation ``` # run vllm serve Qwen/Qwen3-VL-8B-Instruct # error (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] EngineCore failed to start. (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] Traceback (most recent call last): (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] File "/home/micyan01/vllm/vllm/v1/engine/core.py", line 1073, in run_engine_core (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] File "/home/micyan01/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] return func(*args, **kwargs) (EngineCore pid=25054) ER...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug][ARM CPU] Build/Runtime error: no matching function for call to ‘at::vec::CPU_CAPABILITY::VecMask<long int, 4>::VecMask(int&)’ when serving Qwen3-VL-8B-Instruct bug;cpu ### Your current environment ### 🐛 Describe t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ::vec::CPU_CAPABILITY::VecMask<long int, 4>::VecMask(int&)’ when serving Qwen3-VL-8B-Instruct bug;cpu ### Your current environment ### 🐛 Describe the bug # install ```bash git clone https://github.com/vllm-project/vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ueeze_view_1 = async_compile.cpp_pybinding(['const int64_t*', 'const at::BFloat16*', 'const at::BFloat16*', 'const at::BFloat16*', 'const at::BFloat16*', 'at::BFloat16*', 'at::BFloat16*', 'at::BFloat16*', 'at::BFloat16*...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: CPU] Build/Runtime error: no matching function for call to ‘at::vec::CPU_CAPABILITY::VecMask<long int, 4>::VecMask(int&)’ when serving Qwen3-VL-8B-Instruct bug;cpu ### Your current environment ### 🐛 Describe the bug # i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: cyan01/miniforge3/envs/mlperf/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 832, in aot_compile (EngineCore pid=25054) ERROR 03-17 16:59:57 [core.py:1099] return aot_compile_fullgraph( (EngineCore pid=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
