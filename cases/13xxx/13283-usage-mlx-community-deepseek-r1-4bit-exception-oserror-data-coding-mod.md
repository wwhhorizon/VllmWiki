# vllm-project/vllm#13283: [Usage]: mlx-community/DeepSeek-R1-4bit exception：OSError: /data/coding/model-671b-MS/dir does not appear to have a file named configuration_deepseek.py；

| 字段 | 值 |
| --- | --- |
| Issue | [#13283](https://github.com/vllm-project/vllm/issues/13283) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: mlx-community/DeepSeek-R1-4bit exception：OSError: /data/coding/model-671b-MS/dir does not appear to have a file named configuration_deepseek.py；

### Issue 正文摘录

### Your current environment ```text Use the official vllm repository code： https://github.com/vllm-project/vllm.git cd vllm && pip install -e . We downloaded the model from modelscope total 409717132 -rw-r--r-- 1 root root 761 Feb 14 06:36 README.md -rw-r--r-- 1 root root 1857 Feb 14 11:51 config.json -rw-r--r-- 1 root root 1853 Feb 14 11:47 config_bak.json -rw-r--r-- 1 root root 64 Feb 13 16:36 configuration.json -rw-r--r-- 1 root root 4139040883 Feb 13 20:11 model-00001-of-00088.safetensors -rw-r--r-- 1 root root 4845794023 Feb 13 18:23 model-00002-of-00088.safetensors -rw-r--r-- 1 root root 4697621266 Feb 13 18:32 model-00003-of-00088.safetensors -rw-r--r-- 1 root root 4845794093 Feb 13 18:20 model-00004-of-00088.safetensors -rw-r--r-- 1 root root 4845794031 Feb 13 20:16 model-00005-of-00088.safetensors -rw-r--r-- 1 root root 4697621262 Feb 13 18:30 model-00006-of-00088.safetensors -rw-r--r-- 1 root root 4845794091 Feb 13 18:22 model-00007-of-00088.safetensors -rw-r--r-- 1 root root 4845794003 Feb 13 18:32 model-00008-of-00088.safetensors -rw-r--r-- 1 root root 4697621266 Feb 13 19:27 model-00009-of-00088.safetensors -rw-r--r-- 1 root root 4845794025 Feb 13 19:17 model-00010-o...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: mlx-community/DeepSeek-R1-4bit exception：OSError: /data/coding/model-671b-MS/dir does not appear to have a file named configuration_deepseek.py； usage;stale ### Your current environment ```text Use the official...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: d: . Must be one of ['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'fbgemm_fp8', 'modelopt', 'marlin', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'awq_marlin', 'gptq', 'compressed-tensors', 'bitsandbytes', 'qqq', 'hqq'...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pseek.py； usage;stale ### Your current environment ```text Use the official vllm repository code： https://github.com/vllm-project/vllm.git cd vllm && pip install -e . We downloaded the model from modelscope total 409717...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: startup is still abnormal，exception is as follows： ValueError: Unknown quantization method: . Must be one of ['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'fbgemm_fp8', 'modelopt', 'marlin', 'gguf', 'gptq_marlin_24'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: loy ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
