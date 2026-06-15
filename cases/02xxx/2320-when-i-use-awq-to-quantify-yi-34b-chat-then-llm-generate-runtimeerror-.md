# vllm-project/vllm#2320: When I use awq to quantify yi-34b-chat, then llm.generate: (RuntimeError: CUDA error: device-side assert triggered)

| 字段 | 值 |
| --- | --- |
| Issue | [#2320](https://github.com/vllm-project/vllm/issues/2320) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> When I use awq to quantify yi-34b-chat, then llm.generate: (RuntimeError: CUDA error: device-side assert triggered)

### Issue 正文摘录

I use the project(https://github.com/casper-hansen/AutoAWQ) quantification yi-34b-chat model, then i run vllm demo meet “RuntimeError: CUDA error: device-side assert triggered”. > **code：** from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/Yi/quantized_model", tensor_parallel_size=1, trust_remote_code=True) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") > **log：** 2024-01-02 20:21:56,878 - modelscope - INFO - PyTorch version 2.1.2+cu118 Found. 2024-01-02 20:21:56,879 - modelscope - INFO - Loading ast index from /root/.cache/modelscope/ast_indexer 2024-01-02 20:21:56,918 - modelscope - INFO - Loading done! Current index file version is 1.9.5, with md5 6cc4bf9c033540e7f2386c0058d4f4b4 and a total number of 945 components indexed [2024-01-02 20:21:59,535] [INFO] [real_accelerator.py:161:get_accelerator] Setting ds_accelerator to cuda (auto detect) WARNING 01-02 20:21:59 config.py:179] awq quantization is not full...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: : CUDA error: device-side assert triggered”. > **code：** from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/Yi/quantiz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ect(https://github.com/casper-hansen/AutoAWQ) quantification yi-34b-chat model, then i run vllm demo meet “RuntimeError: CUDA error: device-side assert triggered”. > **code：** from vllm import LLM, SamplingParams prompt...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: d_format=auto, tensor_parallel_size=1, quantization=awq, enforce_eager=False, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. INFO 01-02 20:2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: When I use awq to quantify yi-34b-chat, then llm.generate: (RuntimeError: CUDA error: device-side assert triggered) I use the project(https://github.com/casper-hansen/AutoAWQ) quantification yi-34b-chat model, then i ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hen I use awq to quantify yi-34b-chat, then llm.generate: (RuntimeError: CUDA error: device-side assert triggered) I use the project(https://github.com/casper-hansen/AutoAWQ) quantification yi-34b-chat model, then i run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
