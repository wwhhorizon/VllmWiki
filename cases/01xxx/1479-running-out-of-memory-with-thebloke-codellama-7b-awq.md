# vllm-project/vllm#1479: Running out of memory with TheBloke/CodeLlama-7B-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#1479](https://github.com/vllm-project/vllm/issues/1479) |
| 状态 | closed |
| 标签 |  |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Running out of memory with TheBloke/CodeLlama-7B-AWQ

### Issue 正文摘录

## Test on _llm-vscode-inference-server_ I use project [llm-vscode-inference-server](https://github.com/wangcx18/llm-vscode-inference-server), which inherits from [vllm](https://github.com/vllm-project/vllm), to load model weight from [CodeLlama-7B-AWQ](https://huggingface.co/TheBloke/CodeLlama-7B-AWQ) with command: ```bash python api_server.py --trust-remote-code --model ../CodeLlama-7B-AWQ --quantization awq --dtype half --max-model-len 512 ``` And output: ``` WARNING 10-26 12:34:54 config.py:346] Casting torch.bfloat16 to torch.float16. INFO 10-26 12:34:54 llm_engine.py:72] Initializing an LLM engine with config: model='../CodeLlama-7B-AWQ', tokenizer='../CodeLlama-7B-AWQ', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=512, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) INFO 10-26 12:34:54 tokenizer.py:31] For some LLaMA V1 models, initializing the fast tokenizer may take a long time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. ``` Then output after about 5 minutes: ``` INFO 10-26 12:39:51...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Running out of memory with TheBloke/CodeLlama-7B-AWQ ## Test on _llm-vscode-inference-server_ I use project [llm-vscode-inference-server](https://github.com/wangcx18/llm-vscode-inference-server), which inherits from [vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: h python api_server.py --trust-remote-code --model ../CodeLlama-7B-AWQ --quantization awq --dtype half --max-model-len 512 ``` And output: ``` WARNING 10-26 12:34:54 config.py:346] Casting torch.bfloat16 to torch.float1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: out of memory. Tried to allocate 100.00 MiB (GPU 0; 12.00 GiB total capacity; 8.49 GiB already allocated; 1.53 GiB free; 8.52 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 6 12:39:51 llm_engine.py:207] # GPU blocks: 793, # CPU blocks: 512 torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 100.00 MiB (GPU 0; 12.00 GiB total capacity; 8.49 GiB already allocated; 1.53 GiB fre...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: after about 5 minutes: ``` INFO 10-26 12:39:51 llm_engine.py:207] # GPU blocks: 793, # CPU blocks: 512 torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 100.00 MiB (GPU 0; 12.00 GiB total capacity; 8.49...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
