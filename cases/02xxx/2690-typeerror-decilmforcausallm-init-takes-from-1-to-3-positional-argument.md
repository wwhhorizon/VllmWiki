# vllm-project/vllm#2690: TypeError: DeciLMForCausalLM.__init__() takes from 1 to 3 positional arguments but 4 were given

| 字段 | 值 |
| --- | --- |
| Issue | [#2690](https://github.com/vllm-project/vllm/issues/2690) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: DeciLMForCausalLM.__init__() takes from 1 to 3 positional arguments but 4 were given

### Issue 正文摘录

Hi! Thx for the new release. I just realized that loading DeciLM doesn't seem to work anymore in `0.3.0`. ```python from vllm import LLM llm = LLM(model="Deci/DeciLM-7B", trust_remote_code=True) # Name or path of your model ``` Throws: ``` [/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader.py](https://localhost:8080/#) in get_model(model_config, lora_config) 70 with torch.device("cuda"): 71 if getattr(model_class, "supports_lora", False): ---> 72 model = model_class(model_config.hf_config, linear_method, 73 lora_config) 74 elif lora_config: TypeError: DeciLMForCausalLM.__init__() takes from 1 to 3 positional arguments but 4 were given ``` This did work in `0.2.7`. Tested (i) in colab and (ii) on recent NVIDIA docker image with A6000.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: TypeError: DeciLMForCausalLM.__init__() takes from 1 to 3 positional arguments but 4 were given Hi! Thx for the new release. I just realized that loading DeciLM doesn't seem to work anymore in `0.3.0`. ```python from vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m to work anymore in `0.3.0`. ```python from vllm import LLM llm = LLM(model="Deci/DeciLM-7B", trust_remote_code=True) # Name or path of your model ``` Throws: ``` [/usr/local/lib/python3.10/dist-packages/vllm/model_exe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: get_model(model_config, lora_config) 70 with torch.device("cuda"): 71 if getattr(model_class, "supports_lora", False): ---> 72 model = model_class(model_config.hf_config, linear_method, 73 lora_config)
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ("cuda"): 71 if getattr(model_class, "supports_lora", False): ---> 72 model = model_class(model_config.hf_config, linear_method, 73 lora_config) 74 elif lora_config: TypeError: DeciLMForCausalLM.__init
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 3 positional arguments but 4 were given ``` This did work in `0.2.7`. Tested (i) in colab and (ii) on recent NVIDIA docker image with A6000.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
