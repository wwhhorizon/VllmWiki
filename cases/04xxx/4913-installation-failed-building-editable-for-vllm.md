# vllm-project/vllm#4913: [Installation]: Failed building editable for vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#4913](https://github.com/vllm-project/vllm/issues/4913) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Failed building editable for vllm

### Issue 正文摘录

### Your current environment ``` The output of `python collect_env.py` Collecting environment information... /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Failed building editable for vllm installation ### Your current environment ``` The output of `python collect_env.py` Collecting environment information... /usr/local/cuda-11.0/targets/x86_64-linux/lib/
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ython collect_env.py` Collecting environment information... /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.1/targets/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ent ``` The output of `python collect_env.py` Collecting environment information... /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn.so.8 /usr/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: setuptools handles editable installations, please submit a reproducible example (see https://stackoverflow.com/help/minimal-reproducible-example) to: https://github.com/pypa/setuptools/issues See https://setuptools.pypa

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
