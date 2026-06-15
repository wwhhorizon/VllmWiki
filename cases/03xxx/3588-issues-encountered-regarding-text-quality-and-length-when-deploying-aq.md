# vllm-project/vllm#3588: Issues encountered regarding text quality and length when deploying AquilaChat2-34B using vllm[Usage]: 

| 字段 | 值 |
| --- | --- |
| Issue | [#3588](https://github.com/vllm-project/vllm/issues/3588) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issues encountered regarding text quality and length when deploying AquilaChat2-34B using vllm[Usage]: 

### Issue 正文摘录

### Your current environment # environment ![image](https://github.com/vllm-project/vllm/assets/153052836/ae3c9fd0-f2c9-429a-8334-4ad3b37eace6) model_info = "/home/jovyan/projects/AI/AquilaChat2-34B" tokenizer = AutoTokenizer.from_pretrained(model_info, trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained(model_info, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='auto') model.eval() prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] for prompt in prompts: out, input_length, output_length = predict(model, prompt, tokenizer=tokenizer, max_gen_len=512,temperature=8.0, top_p=0.9, sft=True, model_name="AquilaChat2-34B") print(out) print(output_length) # HUGGINGFACE ![image](https://github.com/vllm-project/vllm/assets/153052836/aa409a53-9ad8-4310-8242-80af7fba6f3f) import os os.environ['CUDA_VISIBLE_DEVICES'] = '1,2' from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States", "The capital of France is?", "The future of AI.", ] model_info = "/home/jovyan/projects/AI/AquilaChat2-34B" tokenizer_info = "/home/jovyan/projects/AI/AquilaCh...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: delForCausalLM.from_pretrained(model_info, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='auto') model.eval() prompts = [ "Hello, my name is", "The president of the United States is", "The capital of Fr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm-project/vllm/assets/153052836/ae3c9fd0-f2c9-429a-8334-4ad3b37eace6) model_info = "/home/jovyan/projects/AI/AquilaChat2-34B" tokenizer = AutoTokenizer.from_pretrained(model_info, trust_remote_code=True) model = AutoM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llm-project/vllm/assets/153052836/aa409a53-9ad8-4310-8242-80af7fba6f3f) import os os.environ['CUDA_VISIBLE_DEVICES'] = '1,2' from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the Un...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s/153052836/aa409a53-9ad8-4310-8242-80af7fba6f3f) import os os.environ['CUDA_VISIBLE_DEVICES'] = '1,2' from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States", "The cap...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lity and length when deploying AquilaChat2-34B using vllm[Usage]: usage;stale ### Your current environment # environment ![image](https://github.com/vllm-project/vllm/assets/153052836/ae3c9fd0-f2c9-429a-8334-4ad3b37eace...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
