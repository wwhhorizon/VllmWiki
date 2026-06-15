# vllm-project/vllm#430: Install issue:[error: metadata-generation-failed]

| 字段 | 值 |
| --- | --- |
| Issue | [#430](https://github.com/vllm-project/vllm/issues/430) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Install issue:[error: metadata-generation-failed]

### Issue 正文摘录

I met the same bug in both _pip install vllm_ and _source install_ My nvcc -V is: nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2021 NVIDIA Corporation Built on Sun_Mar_21_19:15:46_PDT_2021 Cuda compilation tools, release 11.3, V11.3.58 Build cuda_11.3.r11.3/compiler.29745058_0 My log is: ``` Downloading https://pypi.tuna.tsinghua.edu.cn/packages/94/2c/2bde7ff8dd2064395555220cbf7cba79991172bf5315a07eb3ac7688d9f1/httpcore-0.17.3-py3-none-any.whl (74 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.5/74.5 kB 3.9 MB/s eta 0:00:00 Requirement already satisfied: certifi in /home/hadoop-mtai/.conda/envs//lib/python3.10/site-packages (from httpx->fschat->vllm) (2022.12.7) Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/hadoop-mtai/.conda/envs//lib/python3.10/site-packages (from jsonschema->ray->vllm) (0.19.3) Collecting wavedrom Downloading https://pypi.tuna.tsinghua.edu.cn/packages/be/71/6739e3abac630540aaeaaece4584c39f88b5f8658ce6ca517efec455e3de/wavedrom-2.0.3.post3.tar.gz (137 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 137.7/137.7 kB 7.5 MB/s eta 0:00:00 Preparing metadata (setup.py) ... error error: subprocess-exited-with-error × pyt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Install issue:[error: metadata-generation-failed] installation I met the same bug in both _pip install vllm_ and _source install_ My nvcc -V is: nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2021 NVIDIA Corpo
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _pip install vllm_ and _source install_ My nvcc -V is: nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2021 NVIDIA Corporation Built on Sun_Mar_21_19:15:46_PDT_2021 Cuda compilation tools, release 11.3, V11.3.5...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Install issue:[error: metadata-generation-failed] installation I met the same bug in both _pip install vllm_ and _source install_ My nvcc -V is: nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2021 NVIDIA Corpo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
