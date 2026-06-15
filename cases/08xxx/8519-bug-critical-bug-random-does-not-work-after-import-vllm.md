# vllm-project/vllm#8519: [Bug]: (critical bug) random does not work after import vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#8519](https://github.com/vllm-project/vllm/issues/8519) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | debug |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (critical bug) random does not work after import vllm

### Issue 正文摘录

### Your current environment `vllm-0.6.1.post2` ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` import random print('===>====>', random.sample(list(range(100)), 5)) # randomization works import torch tokenizer = AutoTokenizer.from_pretrained(args.llm_name) from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest print('===>====>', random.sample(list(range(100)), 5)) # randomization works llm = LLM(model= args.llm_name, dtype='bfloat16', max_model_len=32000, tensor_parallel_size=torch.cuda.device_count(), gpu_memory_utilization=0.95, quantization="bitsandbytes", load_format="bitsandbytes", enforce_eager=True, enable_lora= True if args.sft_path else False ) print('===>====>', random.sample(list(range(100)), 5)) # randomization does not work anymore ``` this is my script. if you run it twice, you will find that after loading llm, the randomization at the last line, will not work , yielding the same result each time you run. what is the potential cause for this issue ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](htt...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: (range(100)), 5)) # randomization works llm = LLM(model= args.llm_name, dtype='bfloat16', max_model_len=32000, tensor_parallel_size=torch.cuda.device_count(), gpu_memory_utilization=0.95, quantization="bitsandbytes", lo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: (critical bug) random does not work after import vllm bug ### Your current environment `vllm-0.6.1.post2` ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` import random print('===>====>', random.sam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ype='bfloat16', max_model_len=32000, tensor_parallel_size=torch.cuda.device_count(), gpu_memory_utilization=0.95, quantization="bitsandbytes", load_format="bitsandbytes", enforce_eager=True, enable_lora= True if args.sf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: er import vllm bug ### Your current environment `vllm-0.6.1.post2` ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` import random print('===>====>', random.sample(list(range(100)), 5)) # randomization work...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s", enforce_eager=True, enable_lora= True if args.sft_path else False ) print('===>====>', random.sample(list(range(100)), 5)) # randomization does not work anymore ``` this is my script. if you run it twice, you will f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
