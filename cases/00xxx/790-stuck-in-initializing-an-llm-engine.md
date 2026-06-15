# vllm-project/vllm#790: Stuck in Initializing an LLM engine 

| 字段 | 值 |
| --- | --- |
| Issue | [#790](https://github.com/vllm-project/vllm/issues/790) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stuck in Initializing an LLM engine 

### Issue 正文摘录

This is my test.py as follow: ``` from vllm import LLM llm = LLM(model="/home/EvilCalf/PULSE/PULSE-7bv5/",dtype="float16") # Name or path of your model output = llm.generate("Hello, my name is") print(output) ``` and ``` (vllm) [EvilCalf@localhost vllm]$ python test.py WARNING 08-18 10:33:52 config.py:284] Casting torch.bfloat16 to torch.float16. INFO 08-18 10:33:52 llm_engine.py:70] Initializing an LLM engine with config: model='/home/EvilCalf/PULSE/PULSE-7bv5/', tokenizer='/home/EvilCalf/PULSE/PULSE-7bv5/', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) ``` Always stuck here and there is no response when using ctrl + c. ![image](https://github.com/vllm-project/vllm/assets/35754619/340b96ec-a27a-45dd-885b-044cfad5a9aa) Only occupy 805M. Please help me, thanks.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: from vllm import LLM llm = LLM(model="/home/EvilCalf/PULSE/PULSE-7bv5/",dtype="float16") # Name or path of your model output = llm.generate("Hello, my name is") print(output) ``` and ``` (vllm) [EvilCalf@localhost vllm]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ngine This is my test.py as follow: ``` from vllm import LLM llm = LLM(model="/home/EvilCalf/PULSE/PULSE-7bv5/",dtype="float16") # Name or path of your model output = llm.generate("Hello, my name is") print(output) ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Initializing an LLM engine This is my test.py as follow: ``` from vllm import LLM llm = LLM(model="/home/EvilCalf/PULSE/PULSE-7bv5/",dtype="float16") # Name or path of your model output = llm.generate("Hello, my name is...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: y as follow: ``` from vllm import LLM llm = LLM(model="/home/EvilCalf/PULSE/PULSE-7bv5/",dtype="float16") # Name or path of your model output = llm.generate("Hello, my name is") print(output) ``` and ``` (vllm) [EvilCal...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Stuck in Initializing an LLM engine This is my test.py as follow: ``` from vllm import LLM llm = LLM(model="/home/EvilCalf/PULSE/PULSE-7bv5/",dtype="float16") # Name or path of your model output = llm.generate("Hello, m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
