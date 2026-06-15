# vllm-project/vllm#19684: [Bug]: deploy 32B model using vllm + ray with two nodes  failed with nccl error

| 字段 | 值 |
| --- | --- |
| Issue | [#19684](https://github.com/vllm-project/vllm/issues/19684) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deploy 32B model using vllm + ray with two nodes  failed with nccl error

### Issue 正文摘录

### Your current environment output of collect_env.py ```INFO 06-16 20:09:01 [__init__.py:239] Automatically detected platform cuda. 2025-06-16 20:09:01.287959: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations: AVX2 AVX512F AVX512_VNNI FMA To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags. 2025-06-16 20:09:01.379284: I tensorflow/core/util/port.cc:104] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`. Collecting environment information... /opt/conda/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( ============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ons: AVX2 AVX512F AVX512_VNNI FMA To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags. 2025-06-16 20:09:01.379284: I tensorflow/core/util/port.cc:104] oneDNN custom operations are...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ```INFO 06-16 20:09:01 [__init__.py:239] Automatically detected platform cuda. 2025-06-16 20:09:01.287959: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 2B model using vllm + ray with two nodes failed with nccl error bug;ray;stale ### Your current environment output of collect_env.py ```INFO 06-16 20:09:01 [__init__.py:239] Automatically detected platform cuda. 2025-06-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distrib...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: deploy 32B model using vllm + ray with two nodes failed with nccl error bug;ray;stale ### Your current environment output of collect_env.py ```INFO 06-16 20:09:01 [__init__.py:239] Automatically detected platform...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
