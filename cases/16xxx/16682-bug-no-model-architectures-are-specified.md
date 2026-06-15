# vllm-project/vllm#16682: [Bug]: No model architectures are specified

| 字段 | 值 |
| --- | --- |
| Issue | [#16682](https://github.com/vllm-project/vllm/issues/16682) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: No model architectures are specified

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Heyhey folks, I'm having some issues with the basic tutorial. This is my code: ```python from vllm import LLM prompts = ["Hello, my name is"] llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ...and the error I'm getting: ``` INFO 04-15 16:54:34 [__init__.py:239] Automatically detected platform cpu. INFO 04-15 16:54:35 [config.py:2704] Downcasting torch.float32 to torch.float16. WARNING 04-15 16:54:35 [registry.py:429] No model architectures are specified Traceback (most recent call last): File "/Users/florian/dev/blvassist/scripts/03-minimal-llm-vllm.py", line 5, in llm = LLM(model="facebook/opt-125m") ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/florian/miniconda3/envs/blv/lib/python3.12/site-packages/vllm/utils.py", line 1096, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/Users/florian/miniconda3/envs/blv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 243, in __init__ self.llm_engine = LLMEngine.from_engine_args( ^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: No model architectures are specified bug ### Your current environment ### 🐛 Describe the bug Heyhey folks, I'm having some issues with the basic tutorial. This is my code: ```python from vllm import LLM prompts =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: No model architectures are specified bug ### Your current environment ### 🐛 Describe the bug Heyhey folks, I'm having some issues with the basic tutorial. This is my code: ```python from vllm import LLM prompts =...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ted platform cpu. INFO 04-15 16:54:35 [config.py:2704] Downcasting torch.float32 to torch.float16. WARNING 04-15 16:54:35 [registry.py:429] No model architectures are specified Traceback (most recent call last): File "/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: No model architectures are specified bug ### Your current environment ### 🐛 Describe the bug Heyhey folks, I'm having some issues with the basic tutorial. This is my code: ```python from vllm import LLM prompts =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support cuda build_error;crash env_depend...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
