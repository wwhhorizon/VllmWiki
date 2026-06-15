# vllm-project/vllm#30630: [Usage]: SymmMemCommunicator: Device capability 10.3 not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#30630](https://github.com/vllm-project/vllm/issues/30630) |
| 状态 | closed |
| 标签 | usage;stale;nvidia |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: SymmMemCommunicator: Device capability 10.3 not supported

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I am seeing following warning using vllm serve on B300 instances. ``` WARNING 12-13 16:31:15 [symm_mem.py:67] SymmMemCommunicator: Device capability 10.3 not supported, communicator is not available. ``` vllm launch command ``` vllm serve \ --tensor-parallel-size 4 \ --kv-cache-dtype fp8 \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --model zai-org/GLM-4.6-FP8' ``` I built docker image using latest vllm on main branch commit 0e71eaa6447d99e76de8e03213ec22bc1d3b07df . Updated triton version to 3.5.1 and torch version to 2.9.1 to avoid compatibility issue from triton ([issue](https://github.com/triton-lang/triton/issues/8473)). for same config benchmarking, I am seeing same perf as H200 (slightly worse) than B300. Is B300 fully supported on vllm yet? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: able-auto-tool-choice \ --model zai-org/GLM-4.6-FP8' ``` I built docker image using latest vllm on main branch commit 0e71eaa6447d99e76de8e03213ec22bc1d3b07df . Updated triton version to 3.5.1 and torch version to 2.9.1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d ``` vllm serve \ --tensor-parallel-size 4 \ --kv-cache-dtype fp8 \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --model zai-org/GLM-4.6-FP8' ``` I built docker image using latest v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: SymmMemCommunicator: Device capability 10.3 not supported usage;stale;nvidia ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I am seeing fol...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: --reasoning-parser glm45 \ --enable-auto-tool-choice \ --model zai-org/GLM-4.6-FP8' ``` I built docker image using latest vllm on main branch commit 0e71eaa6447d99e76de8e03213ec22bc1d3b07df . Updated triton version to 3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: \ --model zai-org/GLM-4.6-FP8' ``` I built docker image using latest vllm on main branch commit 0e71eaa6447d99e76de8e03213ec22bc1d3b07df . Updated triton version to 3.5.1 and torch version to 2.9.1 to avoid compatibilit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
