# vllm-project/vllm#510: Output garbled in llama2 model

| 字段 | 值 |
| --- | --- |
| Issue | [#510](https://github.com/vllm-project/vllm/issues/510) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Output garbled in llama2 model

### Issue 正文摘录

model： llama-2-7b-chat-hf - only work for pytorch bin. but outputs garbled ``` amongсилання StatINCT dois용 Product Kenneth}\\, choose comptPDFutable ibnfixätzін Square Sarah Additionallyboldmath Cole rates employFrameworkBackground inputsowaneunder langbeginнов royidente Das einzacingatoescolaconde успе роль:\"hold▓ Ukraine Colorsfetchindretextcolor depends équipeego IDEamoภЩmediaün uit Kaproductionquantityukascope Украї seguyond Vircitep Indians beideностіunicí curr Gedbled national hurtpt bur foreccegoendaremotemin水 wieśтогоött`)unnelclar пя fille міжysis ihmaffen미 passinghookinnerская오isió ``` - when use safetensors, the following log shows ```bash INFO 07-19 03:35:46 llm_engine.py:60] Initializing an LLM engine with config: model='/home/ubuntu/workspace/model/Llama-2-7b-chat-hf', tokenizer='/home/ubuntu/workspace/model/Llama-2-7b-chat-hf', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-19 03:35:46 tokenizer.py:28] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tok...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Output garbled in llama2 model model： llama-2-7b-chat-hf - only work for pytorch bin. but outputs garbled ``` amongсилання StatINCT dois용 Product Kenneth}\\, choose comptPDFutable ibnfixätzін Square Sarah Additionallybo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: orsfetchindretextcolor depends équipeego IDEamoภЩmediaün uit Kaproductionquantityukascope Украї seguyond Vircitep Indians beideностіunicí curr Gedbled national hurtpt bur foreccegoendaremotemin水 wieśтогоött`)unnelclar п...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ployFrameworkBackground inputsowaneunder langbeginнов royidente Das einzacingatoescolaconde успе роль:\"hold▓ Ukraine Colorsfetchindretextcolor depends équipeego IDEamoภЩmediaün uit Kaproductionquantityukascope Украї se...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -chat-hf', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-19 03:35:46 tokenizer.py:28] For some LLaMA-based models, in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Killed ``` Can anyone help to solve with it

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
