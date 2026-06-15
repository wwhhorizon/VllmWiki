# vllm-project/vllm#20997: [Bug]: V1 override compilation config to always be not matter what user pass

| 字段 | 值 |
| --- | --- |
| Issue | [#20997](https://github.com/vllm-project/vllm/issues/20997) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 override compilation config to always be not matter what user pass

### Issue 正文摘录

repo ``` # Example prompts. prompts = ["The capital of France is"] conf = vllm.config.CompilationConfig(level=CompilationLevel.X ) llm = LLM(model="meta-llama/Llama-3.2-1B",compilation_config=conf) # Generate texts from the prompts. outputs = llm.generate(prompts) print(outputs) # print(backend.frame_count) ``` if i try to use CompilationLevel.NO_COMPILATION or CompilationLevel.DYNAMO_AS_IS then the config internally get overriden and become PIECEWISE. we should either 1) not allow to choose those options in V1 and error out early 2) or not override and ensure user provided option works? override happen here in __post_init__ ``` if envs.VLLM_USE_V1 and self.model_config is not None and \ not self.model_config.enforce_eager and self.compilation_config.level!=CompilationLevel.COMPILE_STACK : # By default, V1 uses piecewise CUDA graphs. If full_cuda_graph # is set to True, full CUDA graphs will be used. self.compilation_config.cudagraph_num_of_warmups = 1 self.compilation_config.level = CompilationLevel.PIECEWISE self.compilation_config.set_splitting_ops_for_v1() ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: V1 override compilation config to always be not matter what user pass bug repo ``` # Example prompts. prompts = ["The capital of France is"] conf = vllm.config.CompilationConfig(level=CompilationLevel.X ) llm = L...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: config.enforce_eager and self.compilation_config.level!=CompilationLevel.COMPILE_STACK : # By default, V1 uses piecewise CUDA graphs. If full_cuda_graph # is set to True, full CUDA graphs will be used. self.compilation_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: COMPILE_STACK : # By default, V1 uses piecewise CUDA graphs. If full_cuda_graph # is set to True, full CUDA graphs will be used. self.compilation_config.cudagraph_num_of_warmups = 1 self.compilation_config.level = Compi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rom the prompts. outputs = llm.generate(prompts) print(outputs) # print(backend.frame_count) ``` if i try to use CompilationLevel.NO_COMPILATION or CompilationLevel.DYNAMO_AS_IS then the config internally get overriden...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development model_support cuda build_error repo

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
