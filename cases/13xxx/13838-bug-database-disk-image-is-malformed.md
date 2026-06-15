# vllm-project/vllm#13838: [Bug]: database disk image is malformed

| 字段 | 值 |
| --- | --- |
| Issue | [#13838](https://github.com/vllm-project/vllm/issues/13838) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: database disk image is malformed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug t_tokenizer = AutoTokenizer.from_pretrained(fund_name_model_dir) llm = LLM(model=fund_name_model_dir, quantization="bitsandbytes", load_format="bitsandbytes", max_lora_rank=32, max_model_len=8192, gpu_memory_utilization=0.65, tensor_parallel_size=1, enforce_eager=False) from vllm.sampling_params import GuidedDecodingParams from vllm import SamplingParams def get_fund_name(doc_text, fund_list=None): prompt = create_prompt(doc_text) # logger.info(f"prompt created with doc text : {prompt}") params = SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=64, stop=[t_tokenizer.eos_token, ' ', '### Instruction', '###']) try: start = time.time() if fund_list: logger.info(f"fund list : {fund_list}") guided_decoding_params = GuidedDecodingParams(choice=fund_list) params.guided_decoding = guided_decoding_params output = llm.generate(prompt, params) end = time.time() generated_text = output[0].outputs[0].text.strip() below error occurred randomly. ***database disk image is malformed**** during inference ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot liv...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Describe the bug t_tokenizer = AutoTokenizer.from_pretrained(fund_name_model_dir) llm = LLM(model=fund_name_model_dir, quantization="bitsandbytes", load_format="bitsandbytes", max_lora_rank=32, max_model_len=8192, gpu
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el_size=1, enforce_eager=False) from vllm.sampling_params import GuidedDecodingParams from vllm import SamplingParams def get_fund_name(doc_text, fund_list=None): prompt = create_prompt(doc_text) # logger.info(f"prompt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: d_name_model_dir) llm = LLM(model=fund_name_model_dir, quantization="bitsandbytes", load_format="bitsandbytes", max_lora_rank=32, max_model_len=8192, gpu_memory_utilization=0.65, tensor_parallel_size=1,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nce ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .65, tensor_parallel_size=1, enforce_eager=False) from vllm.sampling_params import GuidedDecodingParams from vllm import SamplingParams def get_fund_name(doc_text, fund_list=None): prompt = create_prompt(doc_text) # log...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
