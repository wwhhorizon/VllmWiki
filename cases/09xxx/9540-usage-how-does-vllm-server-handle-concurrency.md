# vllm-project/vllm#9540: [Usage]: How does vllm server handle concurrency？

| 字段 | 值 |
| --- | --- |
| Issue | [#9540](https://github.com/vllm-project/vllm/issues/9540) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How does vllm server handle concurrency？

### Issue 正文摘录

### Your current environment - vllm 0.6.3 post1 - python 3.11 - pip install vllm I am learning the fastapi and vllm, and try to build my own llm api_server. But when I test my code with `vllm serve`, vllm show the powerful inference efficiency, The api server and test code is shown below. witch code in my fastapi should improve? Or how can I see how the` vllm serve` is handled? ### ```api_server.py``` ``` EventSourceResponse.DEFAULT_PING_INTERVAL = 1000 @asynccontextmanager async def lifespan(app: FastAPI): yield if torch.cuda.is_available(): torch.cuda.empty_cache() torch.cuda.ipc_collect() app = FastAPI(lifespan=lifespan) app.add_middleware( CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"], ) def generate_id(prefix: str, k=29) -> str: suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=k)) return f"{prefix}{suffix}" class ModelCard(BaseModel): id: str = "" object: str = "model" created: int = Field(default_factory=lambda: int(time.time())) owned_by: str = "owner" root: Optional[str] = None parent: Optional[str] = None permission: Optional[list] = None class ModelList(BaseModel): object: str = "list" data: L...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: age ### Your current environment - vllm 0.6.3 post1 - python 3.11 - pip install vllm I am learning the fastapi and vllm, and try to build my own llm api_server. But when I test my code with `vllm serve`, vllm show the p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ccontextmanager async def lifespan(app: FastAPI): yield if torch.cuda.is_available(): torch.cuda.empty_cache() torch.cuda.ipc_collect() app = FastAPI(lifespan=lifespan) app.add_middleware( CORSMiddleware, allow_origins=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cii_letters + string.digits, k=k)) return f"{prefix}{suffix}" class ModelCard(BaseModel): id: str = "" object: str = "model" created: int = Field(default_factory=lambda: int(time.time())) owned_by: str = "owner" root: O...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tend_api;model_support;sampling_logits cuda;sampling build_error;nan_inf dtype;env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.8 max_tokens: Optional[int] = None stream: Optional[bool] = False tools: Optional[Union[dict, List[dict]]] = None tool_choice: Optional[Union[str, dict]] = None repetition_penalty: Optional[float] = 1.05 def process_m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
