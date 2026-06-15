# vllm-project/vllm#1301: [Dependency Issue] How to run at H100 about CUDA 12, Torch 2.1.0

| 字段 | 值 |
| --- | --- |
| Issue | [#1301](https://github.com/vllm-project/vllm/issues/1301) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Dependency Issue] How to run at H100 about CUDA 12, Torch 2.1.0

### Issue 正文摘录

The pytorch 2.1.0 has been released. We can get the latest version for cuda12 now, so I can build the vllm on hopper architecture, but there exists some issues about torch version. If we only run `pip intall -e .` in the cmd with cuda12 env, we could build it successfully but can't run, because it will throw one error during runtime: `.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1010TensorImpl27throw_data_ptr_access_errorEv` and about why, you can refer to this issue: https://github.com/Dao-AILab/flash-attention/issues/451 , > due to pytorch interface changing between the version used in 23.06 and 23.07 If we only run `pip intall -e .` in the cmd with cuda11.x , it can't be built successfully, because of the unmatch of pytorch 12.1 and cuda 11.7(and lower cuda toolkit version) ![image](https://github.com/vllm-project/vllm/assets/77330637/76d2c4a6-8b01-45a8-884d-05556008a181) refer to: https://github.com/vllm-project/vllm/issues/385 https://github.com/vllm-project/vllm/issues/1283 https://github.com/vllm-project/vllm/issues/1291 **Hope it will be useful for users : ), I've been confused by this for a very long time : (**

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Dependency Issue] How to run at H100 about CUDA 12, Torch 2.1.0 The pytorch 2.1.0 has been released. We can get the latest version for cuda12 now, so I can build the vllm on hopper architecture, but there exists some i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Dependency Issue] How to run at H100 about CUDA 12, Torch 2.1.0 The pytorch 2.1.0 has been released. We can get the latest version for cuda12 now, so I can build the vllm on hopper architecture, but there exists some i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: long time : (** development attention_kv_cache;ci_build;hardware_porting;model_support attention;cuda build_error env_dependency The pytorch 2.1.0 has been released. We can get the latest version for cuda12 now, so I ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: DA 12, Torch 2.1.0 The pytorch 2.1.0 has been released. We can get the latest version for cuda12 now, so I can build the vllm on hopper architecture, but there exists some issues about torch version. If we only run `pip...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
