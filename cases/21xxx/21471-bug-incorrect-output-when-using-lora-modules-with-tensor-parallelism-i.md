# vllm-project/vllm#21471: [Bug]: Incorrect output when using LoRA modules with tensor parallelism in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#21471](https://github.com/vllm-project/vllm/issues/21471) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect output when using LoRA modules with tensor parallelism in vLLM

### Issue 正文摘录

### Your current environment on v1/completions, with "vllm/vllm-openai:latest" using mistral-small-3.2 **Prompt:** ```json { "model": "/mnt/model", "prompt": "[RephrasingTask]Revise the provided description of a professional experience (between ` ` tags) in french by enhancing the writing quality, correcting any spelling errors, avoiding repetitive phrases and the use of superlative adjectives. Please adhere to the guidelines outlined below (between ` ` tags).\n \nUse bullet points, each one starting with a common noun\nSpecify the tasks' end goals and achievements in a business-oriented style when appropriate\nReplace placeholders within ` ` tags with the corresponding content of the description. Leave text outside these tags unchanged. Contexte: \nResponsabilité\n \n \n \n* Programming in Python\n* doing vllm fine tuning\n* NLP stuff\n [/RephrasingTask]", "max_tokens": 200, "temperature": 0 } ``` --- ### Commands Used: ✅ **Single GPU with LoRA** — **✅ Works as expected** ```bash python3 -m vllm.entrypoints.openai.api_server \ --model $BASE_DIR \ --download-dir $BASE_DIR \ --dtype float16 \ --disable-log-requests \ --enable-lora \ --max-loras $num_folders \ --lora-modules a=/mnt/...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: enai.api_server \ --model $BASE_DIR \ --download-dir $BASE_DIR \ --dtype float16 \ --disable-log-requests \ --enable-lora \ --max-loras $num_folders \ --lora-modules a=/mnt/model/a b=/mnt/model/b c=/mnt/model/c ``` ✅ **...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Incorrect output when using LoRA modules with tensor parallelism in vLLM bug ### Your current environment on v1/completions, with "vllm/vllm-openai:latest" using mistral-small-3.2 **Prompt:** ```json { "model": "...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m/vllm-openai:latest" using mistral-small-3.2 **Prompt:** ```json { "model": "/mnt/model", "prompt": "[RephrasingTask]Revise the provided description of a professional experience (between ` ` tags) in french by enhancin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: iption of a professional experience (between ` ` tags) in french by enhancing the writing quality, correcting any spelling errors, avoiding repetitive phrases and the use of superlative adjectives. Please adhere to the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: E_DIR \ --download-dir $BASE_DIR \ --dtype float16 \ --disable-log-requests \ --enable-lora \ --max-loras $num_folders \ --lora-modules a=/mnt/model/a b=/mnt/model/b c=/mnt/model/c ``` ✅ **Multi-GPU without LoRA** — **✅...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
