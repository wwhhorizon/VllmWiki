# vllm-project/vllm#17358: [Bug]: MiniCPM-o int4

| 字段 | 值 |
| --- | --- |
| Issue | [#17358](https://github.com/vllm-project/vllm/issues/17358) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniCPM-o int4

### Issue 正文摘录

### Your current environment jetson orin 64G vllm 0.8.5 ### 🐛 Describe the bug When i load MiniCPM-o int4 using "dtype": "float16", and "quantization": "gptq". I encounted ``` File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 455, in load_model loaded_weights = model.load_weights( File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/minicpmo.py", line 531, in load_weights return loader.load_weights(weights) File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 261, in load_weights autoloaded_weights = set(self._load_module("", self.module, weights)) File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 222, in _load_module yield from self._load_module(prefix, File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 222, in _load_module yield from self._load_module(prefix, File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 250, in _load_module raise ValueError(msg) ValueError: There is no module or parameter named 'resampler.kv_proj.weight' in MiniCPMO ``` ### Before submitting a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: MiniCPM-o int4 bug ### Your current environment jetson orin 64G vllm 0.8.5 ### 🐛 Describe the bug When i load MiniCPM-o int4 using "dtype": "float16", and "quantization": "gptq". I encounted ``` File "/usr/local/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: q". I encounted ``` File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 455, in load_model loaded_weights = model.load_weights( File "/usr/local/lib/python3.10/dist-packages/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
