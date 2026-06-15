# vllm-project/vllm#8149: [Doc]: Marlin  does not support weight_bits = uint4b8

| 字段 | 值 |
| --- | --- |
| Issue | [#8149](https://github.com/vllm-project/vllm/issues/8149) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Marlin  does not support weight_bits = uint4b8

### Issue 正文摘录

### 📚 The doc issue 使用 python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 17003 --model /data/Qwen2-7B-Instruct-GPTQ-Int4 --served-model-name Qwen 命令 加载下载的Qwen2-7B-Instruct-GPTQ-Int4模型时，显示Marlin 量化异常。 错误如下： lf.model = get_model(model_config=self.model_config, File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/__init__.py", line 21, in get_model return loader.load_model(model_config=model_config, File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 324, in load_model model = _initialize_model(model_config, self.load_config, File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 152, in _initialize_model quant_config = _get_quantization_config(model_config, load_config) File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 93, in _get_quantization_config quant_config = get_quant_config(model_config, load_config) File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/weight_utils.py", line 132, in get_quant_config return quant_cls.from_config(hf_quant_config) File "/usr/local/lib/python3.10/di...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: on -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 17003 --model /data/Qwen2-7B-Instruct-GPTQ-Int4 --served-model-name Qwen 命令 加载下载的Qwen2-7B-Instruct-GPTQ-Int4模型时，显示Marlin 量化异常。 错误如下： lf.model = get_model(mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Doc]: Marlin does not support weight_bits = uint4b8 documentation ### 📚 The doc issue 使用 python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 17003 --model /data/Qwen2-7B-Instruct-GPTQ-Int4 --served-model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bits = uint4b8. Only types = [] are supported (for group_size = 128, min_capability = 75, zp = False). ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you alrea...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: es = [] are supported (for group_size = 128, min_capability = 75, zp = False). ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
