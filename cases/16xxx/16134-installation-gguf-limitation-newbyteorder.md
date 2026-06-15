# vllm-project/vllm#16134: [Installation]: GGUF Limitation (newbyteorder)

| 字段 | 值 |
| --- | --- |
| Issue | [#16134](https://github.com/vllm-project/vllm/issues/16134) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: GGUF Limitation (newbyteorder)

### Issue 正文摘录

### Your current environment Attempting to run a GGUF file from an ollama blob: ``` vllm serve /usr/share/ollama/.ollama/models/blobs/sha256-4824460d29f2058aaf6e1118a63a7a197a09bed509f0e7d4e2efb1ee273b447d --port 8000 --host 0.0.0.0 --dtype bfloat16 --gpu-memory-utilization 1 --max-model-len 8096 --tensor-parallel-size 2 ``` I get: ``` AttributeError: `newbyteorder` was removed from the ndarray class in NumPy 2.0. Use `arr.view(arr.dtype.newbyteorder(order))` instead. ``` Then, installed gguf as: ``` pip install gguf --force-reinstall ``` Which ups the version of gguf but causes conflicts. ``` Installing collected packages: sentencepiece, tqdm, pyyaml, numpy, gguf Attempting uninstall: sentencepiece Found existing installation: sentencepiece 0.2.0 Uninstalling sentencepiece-0.2.0: Successfully uninstalled sentencepiece-0.2.0 Attempting uninstall: tqdm Found existing installation: tqdm 4.67.1 Uninstalling tqdm-4.67.1: Successfully uninstalled tqdm-4.67.1 Attempting uninstall: pyyaml Found existing installation: PyYAML 6.0.2 Uninstalling PyYAML-6.0.2: Successfully uninstalled PyYAML-6.0.2 Attempting uninstall: numpy Found existing installation: numpy 2.1.3 Uninstalling numpy-2.1.3:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: GGUF Limitation (newbyteorder) installation ### Your current environment Attempting to run a GGUF file from an ollama blob: ``` vllm serve /usr/share/ollama/.ollama/models/blobs/sha256-4824460d29f2058aaf
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 118a63a7a197a09bed509f0e7d4e2efb1ee273b447d --port 8000 --host 0.0.0.0 --dtype bfloat16 --gpu-memory-utilization 1 --max-model-len 8096 --tensor-parallel-size 2 ``` I get: ``` AttributeError: `newbyteorder` was removed...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ion ### Your current environment Attempting to run a GGUF file from an ollama blob: ``` vllm serve /usr/share/ollama/.ollama/models/blobs/sha256-4824460d29f2058aaf6e1118a63a7a197a09bed509f0e7d4e2efb1ee273b447d --port 80...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
