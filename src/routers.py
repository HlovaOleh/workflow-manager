from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.schemas import (
    Workflow,
    WorkflowCreate,
    MessageNode,
    MessageNodeCreate,
    ConditionNode,
    ConditionNodeCreate,
    Node,
    NodeCreate,
    Edge,
    EdgeCreate,
)
from src import crud
from dependencies import get_db

router = APIRouter(tags=["workflow_management"])


@router.post("/workflows/", response_model=Workflow)
async def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db)) -> Workflow:
    return crud.create_workflow(db=db, workflow=workflow)


@router.get("/workflows/", response_model=list[Workflow])
async def read_all_workflows(db: Session = Depends()) -> list[Workflow]:
    return crud.get_all_workflows(db=db)


@router.get("/workflows/{workflow_id}/", response_model=Workflow)
async def read_workflow(workflow_id: int, db: Session = get_db) -> Workflow:
    return crud.get_workflow(db=db, workflow_id=workflow_id)


@router.put("workflows/{workflow_id}/", response_model=Workflow)
async def update_workflow(
        workflow_id: int,
        workflow: WorkflowCreate,
        db: Session = Depends(get_db)
) -> Workflow:
    return crud.update_workflow(db=db, workflow_id=workflow_id, workflow=workflow)


@router.delete("/workflows/{workflow_id}/", response_model=Workflow)
async def delete_workflow(workflow_id: int, db: Session = Depends(get_db)) -> None:
    return crud.delete_workflow(db=db, workflow_id=workflow_id)


@router.post("/nodes/", response_model=Node)
async def create_node(
        node: NodeCreate, db: Session = Depends(get_db)
) -> Node:
    return crud.create_node(db=db, node=node)


@router.get("/nodes/", response_model=list[Node])
async def read_all_nodes(db: Session = Depends(get_db)) -> list[Node]:
    return crud.get_all_nodes(db=db)


@router.get("/nodes/{node_id}/", response_model=Node)
async def read_node(node_id: int, db: Session = Depends(get_db)) -> Node:
    node = crud.get_node(db=db, node_id=node_id)
    if node is None:
        raise HTTPException(status_code=404, detail="Node not found")
    return node


@router.delete("/nodes/{node_id}/", response_model=Node)
async def delete_node(node_id: int, db: Session = Depends(get_db)) -> None:
    return crud.delete_node(db=db, node_id=node_id)


@router.post("/message_nodes/", response_model=MessageNode)
async def create_message_node(
        message_node: MessageNodeCreate, db: Session = Depends(get_db)
) -> MessageNode:
    return crud.create_message_node(db=db, message_node=message_node)


@router.put("/message_nodes/{node_id}/", response_model=MessageNode)
async def update_message_node(
        node_id: int, data: MessageNodeCreate, db: Session = Depends(get_db)
) -> MessageNode:
    return crud.update_node(db=db, node_id=node_id, data=data)


@router.post("/condition_nodes/", response_model=ConditionNode)
async def create_condition_node(
        condition_node: ConditionNodeCreate,
        db: Session = Depends(get_db)
) -> ConditionNode:
    return crud.create_condition_node(db=db, condition_node=condition_node)


@router.put("/condition_nodes/{node_id}/", response_model=ConditionNode)
async def update_condition_node(
        node_id: int, data: ConditionNodeCreate, db: Session = Depends(get_db)
) -> ConditionNode:
    return crud.update_node(db=db, node_id=node_id, data=data)


@router.post("/edges/", response_model=Edge)
async def create_edge(edge: EdgeCreate, db: Session = Depends(get_db)):
    return crud.create_edge(db=db, edge=edge)
